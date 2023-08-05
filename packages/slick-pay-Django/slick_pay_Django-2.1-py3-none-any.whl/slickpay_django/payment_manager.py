from slickpay_lib.constant import SLICKPAY_API_URL
from slickpay_lib.sync_lib.webhook import PaymentManager
from django.conf import settings

_api_url: str
try:
    _api_url = settings.SLICKPAY_API_URL
except Exception as e:
    _api_url = SLICKPAY_API_URL

payment_manager = PaymentManager( _api_url
)
