import json
import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, FormView
from django.views.generic.detail import DetailView, BaseDetailView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import requests
from django.conf import settings

from slickpay_lib.constant import (
    PAYMENT_CANCELED,
    PAYMENT_PAID,
    PAYMENT_FAILED,
    PAYMENT_IN_PROGRESS,
)

#from slick_pay_django.forms import FakePaymentForm

from slick_pay_django.models import AbstractPayment
from slick_pay_django.payment_manager import payment_manager



# logger = logging.getLogger("chargily-app")


class ValidationError(Exception):
    pass


# -----------
# MXIN
# -----------
class OnlyFinishedPaymentMixin:
    def get_queryset(self):
        return self.model._default_manager.filter(
            status__in=[
                PAYMENT_PAID,
                PAYMENT_FAILED,
                PAYMENT_CANCELED,
            ]
        )


# -----------
# VIEW
# -----------
@method_decorator(csrf_exempt, name="dispatch")
class PaymentConfirmationView(View):
    required_body_options = {
        "status",
        "errors",
        "msg",
        "transfer_id",
        "url",
    }

    manager = payment_manager
    model = None

    def post(self, request: HttpRequest, *args, **kwargs):
        self.get_args(request)
        try:
            #self.validate_signature()
            self.validate_args()
            #self.confirmation()
        except ValidationError as e:
            # LOG here
            pass

        return HttpResponse()


    def get_args(self, request: HttpRequest):
        #self.request_signature = request.headers.get("Signature")
        self.raw_body = request.body

        self.request_body = json.loads(request.body)

        if self.request_body:
            self.invoice: dict = self.request_body.get("invoice") or None

    def validate_args(self) -> bool:
        if not self.request_signature:
            return False

        if not hasattr(self, "request_body"):
            return False

        if not hasattr(self, "invoice"):
            return False

        if not isinstance(self.invoice, dict):
            return False

        request_args = set(self.invoice.keys())

        if not self.required_body_options.issubset(request_args):
            return False

        return True



    def get_object(self, invoice_number):
        object = self.model.objects.get(invoice_number=invoice_number)
        return object

    def payment_success(self, object: AbstractPayment, **kwargs):
        object.payment_confirm(**kwargs)

    def payment_failed(self, object: AbstractPayment, **kwargs):
        object.payment_failed(**kwargs)

    def payment_canceled(self, object: AbstractPayment, **kwargs):
        object.payment_canceled(**kwargs)

class ConfirmView(View):
    required_body_options = {
        "c",
        "date",
        "items"
        "amount",
        "errors"
        "orderId",
        "invoice_num",
        "msg",
        "orderNumber",
        "approvalCode",
        "respCode_desc"
    }

    manager = payment_manager
    model = None

    def get(self, request: HttpRequest, *args, **kwargs) -> requests.Response :
        transfer_id = request.GET.get('transfer_id')
        rib = request.GET.get('rib')
        data = {
                'rib' :settings.RIB,
                'transfer_id' :transfer_id}
        print("transfer_id", transfer_id)
        print("data", data)
        headers = { "Accept": "application/json"}
        print("befor request")
        response = requests.post("https://slickpay.azimutbscenter.com/api/slickapiv1/transfer/transferPaymentSatimCheck",
                                 headers=headers, json=data)

        print("response",json.loads(response.content))
        print("after request")
        return JsonResponse(json.loads(response.content))
        #return render(request,'sponsor/sponsor_status.html')
        #return HttpResponse()

    def validate_signature(self) -> bool:
        valide = self.manager.make_confirmation(self.raw_body, self.request_signature)
        if not valide:
            raise ValidationError()

    def get_args(self, request: HttpRequest):
        self.request_signature = request.headers.get("Authorization")
        self.raw_body = request.body

        self.request_body = json.loads(request.body)

        if self.request_body:
            self.invoice: dict = self.request_body.get("invoice") or None

    def validate_args(self) -> bool:
        if not self.request_signature:
            return False

        if not hasattr(self, "request_body"):
            return False

        if not hasattr(self, "invoice"):
            return False

        if not isinstance(self.invoice, dict):
            return False

        request_args = set(self.invoice.keys())

        if not self.required_body_options.issubset(request_args):
            return False

        return True




    def get_object(self, invoice_number):
        object = self.model.objects.get(invoice_number=invoice_number)
        return object

    def payment_success(self, object: AbstractPayment, **kwargs):
        object.payment_confirm(**kwargs)

    def payment_failed(self, object: AbstractPayment, **kwargs):
        object.payment_failed(**kwargs)

    def payment_canceled(self, object: AbstractPayment, **kwargs):
        object.payment_canceled(**kwargs)

class CreatePaymentView(CreateView):
    payment_create_faild_url = None

    def form_valid(self, form) -> HttpResponse:
        self.create_object(form)

        payment_url = self.object.make_payment()
        if payment_url:
            return HttpResponseRedirect(redirect_to=payment_url)

        print("failed")
        return self.payment_create_faild()

    def create_object(self, form):
        self.object: AbstractPayment = form.save()

    def payment_create_faild(self):
        return HttpResponseRedirect(redirect_to=self.payment_create_faild_url)


class PaymentObjectStatusView(DetailView):
    model: AbstractPayment = None
    slug_field: str = "invoice_number"
    slug_url_kwarg = "invoice_number"


class PaymentObjectDoneView(OnlyFinishedPaymentMixin, PaymentObjectStatusView):
    pass





# class CreatePaymentJSON(CreatePaymentView):
#     def form_valid(self, form) -> HttpResponse:
#         self.create_object()
#         payment_url = self.object.make_payment()
#         if payment_url:
#             return JsonResponse({"redirect_url": payment_url, "status": "success"})
#         return JsonResponse(
#             {"redirect_url": self.payment_create_faild_url, "status": "failed"}
#         )
