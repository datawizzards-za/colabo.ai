# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
# Create your views here.


class Home(View):
    template_name = 'app/index.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, args, **kwarg):
        return render(request, self.template_name)
