

import json

from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class ReactView(View):
    initial_state = None
    template_name = None

    def get_template_name(self):
        return self.template_name

#   def set_initial_state(self, component, state):
#       self.initial_state[component] = json.loads(state)
#       return self.initial_state

    def get_context_data(self, **kwargs):
        context_data = {}
        return context_data 

    def get(self, request, *args, **kwargs):
        template = self.get_template_name()
        template_data = self.get_context_data()
        #   template_data['initial_state'] = json.dumps(initial_state)

        self.request = request
        # self.args = args
        # self.kwargs = kwargs
        
        response = render(request, template, template_data)

        return response
