from django.conf.urls import url
from accounts.views import AccountsLandingView

urlpatterns = [
    url(r'cuentas/$', AccountsLandingView.as_view(), name="accounts")
]
