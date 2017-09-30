# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from rest_framework import generics

from app.utils import topics
import pickle
import pandas as pd
import numpy as np
from app.models import Employee

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

class GetData(generics.ListAPIView):
    def get_queryset(self):
        title_desc = pickle.load(open('data/johannesburg.pkl', 'r'))
        names = pickle.load(open('data/employee_names.pkl', 'r'))

        name_ = [{'full_names': name[0], 'gender':"Male" if name[1] == "Mr" else "Female"} for name in names]
        df1 = pd.DataFrame(title_desc)
        df2 = pd.DataFrame(name_)
        df = pd.concat([df1,df2], axis=1)
        skill = pickle.load(open('data/skills.pkl', 'r'))

        def sk(skill):
            a = np.arange(len(skill))
            np.random.shuffle(a)
            skills = [[skill[i],i] for i in a[:11]]
            return skills

        df['skill'] = df['id'].apply(lambda x: sk(skill))
        interests = open('data/interests.txt', 'r').readlines()
        interest = [array.replace('\n','') for array in interests]


        def rates(interest):
            a = np.arange(len(interest))
            np.random.shuffle(a)
            interest = [[interest[i],i] for i in a[:11]]
            return interest

        df['interests'] = df['id'].apply(lambda x: rates(interest))


