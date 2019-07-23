from django.conf.urls import url
from account.views import AccountLandingView

urlpatterns = [
    url(r'cuentas/$', AccountLandingView.as_view(), name="account")
]
