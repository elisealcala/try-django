from django.shortcuts import render
from react.views import ReactView

# Create your views here.
class AccountLandingView(ReactView):
    template_name = 'account/account_landing.html'

