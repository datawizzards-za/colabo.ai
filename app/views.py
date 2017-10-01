# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import View
from rest_framework import generics, serializers

from app.utils import topics
import pickle
import pandas as pd
import numpy as np
from app.models import Employee, Skill, Interest, Project, Topic, Meeting, \
    Review, MeetingStatus


class Home(View):
    template_name = 'app/index.html'

    def get(self, request):
        data = pickle.load(open('data/johannesburg.pkl', 'r'))
        data_samples = [d['description'] for d in data]
        headlines = topics.compute_nmf(data_samples)
        similarity = topics.compute_similarity(data_samples)
        print similarity
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

        name_ = [{'full_names': name[0], 'gender':True if name[1] == "Mr" else
                  False} for name in names]
        df1 = pd.DataFrame(title_desc)
        df2 = pd.DataFrame(name_)
        df = pd.concat([df1, df2], axis=1)
        skill = pickle.load(open('data/skills.pkl', 'r'))

        def sk(skill):
            a = np.arange(len(skill))
            np.random.shuffle(a)
            skills = [[skill[i], i] for i in a[:11]]
            return skills

        df['skill'] = df['id'].apply(lambda x: sk(skill))
        interests = open('data/interests.txt', 'r').readlines()
        #interest = [array.replace('\n','') for array in interests]

        def rates(interest):
            a = np.arange(len(interest))
            np.random.shuffle(a)
            interest = [[interest[i], i] for i in a[:11]]
            return interest

        #df['interests'] = df['id'].apply(lambda x: rates(interest))
        def data_employee():
            for item in range(len(df)):
                Employee.objects.create(full_names=df[
                    'full_names'][item], gender=df['gender'][item],
                    job_desc=df['description'][item],
                    job_title=df['job_title'][item])

        def skills_insert(df):
            """
            # Step one: store all skills
            skills = pickle.load(open('data/skills.pkl', 'r'))

            for skill in skills:
                Skill.objects.get_or_create(name=skill)

            # Step two: associate skill with people
            for emp in Employee.objects.all():
               num = np.random.randint(8, 15)
               skills = Skill.objects.all().order_by('?')[:num]

               for skill in skills:
                   if skill not in emp.skills.all():
                       emp.skills.add(skill)
            """
            # Step three: interests
            # for emp in Employee.objects.all():

            #    pass
            """
            for item in range(len(df)):
                employee =  Employee.objects.get(emp_id=df['id'][item])
                for skill in df['skill'][item]:
                    obj_skill = Skill.objects.get_or_create(name = skill[0])
                    found = False
                    print obj_skill
                    for a in employee.skills.all():
                        if a.name == obj_skill.name:
                            found = True
                            break

                    if not found:
                        employee.skills.add(obj_skill)
            """

        skills_insert(df)

#################### serializers #########################################


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['emp_id', 'full_names', 'job_title', 'job_desc']


class EmployeeDetails(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        data = pickle.load(open('data/johannesburg.pkl', 'r'))
        data_samples = [d['description'] for d in data]
        return topics.compute_similarity(data_samples)

class EmployeeRandomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['emp_id', 'full_names', 'job_title', 'job_desc']


class EmployeeRandomDetails(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        data = pickle.load(open('data/johannesburg.pkl', 'r'))
        data_samples = [d['description'] for d in data]
        return topics.compute_similarity(data_samples)

class EmployeeRandomXSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = ['emp_id', 'full_names', 'job_title', 'job_desc']


class EmployeeRandomXDetails(generics.ListAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        data = pickle.load(open('data/johannesburg.pkl', 'r'))
        data_samples = [d['description'] for d in data]
        return topics.computex_similarity(data_samples)