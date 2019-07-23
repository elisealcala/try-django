from django.shortcuts import render
from react.views import ReactView

# Create your views here.
class AccountsLandingView(ReactView):
    template_name = 'accounts/accounts_landing.html'

