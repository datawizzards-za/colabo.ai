# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from rest_framework import generics

from app.utils import topics
import pickle


class Home(View):
    template_name = 'app/index.html'

    def get(self, request):
        data = pickle.load(open('data/johannesburg.pkl', 'r'))
        data_samples = [d['description'] for d in data]
        headlines = topics.compute_nmf(data_samples)
        context = {'headlines': headlines}
        return render(request, self.template_name, context)

    def post(self, request, args, **kwarg):
        return render(request, self.template_name)


class SignIn(View):
    template_name = 'app/signin.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, args, **kwarg):
        return render(request, self.template_name)


class SignUp(View):
    template_name = 'app/signup.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, args, **kwarg):
        return render(request, self.template_name)


############################## API VIEWS #####################################


class GetSystemOrderDetails(generics.ListAPIView):
    def get_queryset(self):
        order_number = self.kwargs['user_number']
        data = pickle.load(open('data/johannesburg.pkl', 'r'))
        data_samples = [d['description'] for d in data]
        headlines = topics.compute_nmf(data_samples)
        context = {'headlines': headlines}
        return context
