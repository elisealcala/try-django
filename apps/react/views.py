"""
high level support for doing this and that.
"""

import json

from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class ReactView(View):
    initial_state = None
    template_name = None

    def __init__(self, **kwargs):
        super(ReactView, self).__init__(**kwargs)
        self.initial_state = {
            'user': {},
            'ab_tests': {},
            'asdasd': 'ssad'
        }

    def get_template_name(self):
        return self.template_name

    def get_context_data(self, **kwargs):
        context_data = {}
        context_data.update(kwargs)
        return context_data

    def set_initial_state(self, component, state):
        print(state)
        self.initial_state[component] = json.loads(state)

    def get_initial_state(self):
        return self.initial_state

    def get(self, request, *args, **kwargs):
        template = self.get_template_name()
        context_data = self.get_context_data()
        context_data['initial_state'] = self.get_initial_state()

        self.request = request
        self.args = args
        self.kwargs = kwargs
        
        response = render(request, template, context_data)

        return response
