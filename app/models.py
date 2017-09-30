# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True, unique=True)
    full_names = models.CharField(max_length=100)
    gender = models.BooleanField()
    job_desc = models.CharField(max_length=10000)
    job_title = models.CharField(max_length=1000)


class Skill(models.Model):
    class Meta:
        unique_together = (('name', 'emp_id'))
    
    name = models.CharField(primary_key=True, max_length=100)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Interest(models.Model):
    class Meta:
        unique_together = (('name', 'emp_id'))
    
    name = models.CharField(primary_key=True, max_length=100)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class Project(models.Model):
    proj_id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    proj_lead = models.ForeignKey(Employee, on_delete=models.CASCADE) 
    proj_lead = models.ForeignKey(
        Employee,
        related_name='%(class)s_lead',
        on_delete=models.CASCADE
    )
    skill_req = models.CharField(max_length=10000)
    team = models.ManyToManyField(Employee, related_name='%(class)s_team')
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)


class Topic(models.Model):
    topic_id = models.AutoField(primary_key=True, unique=True)
    text = models.CharField(max_length=1000)


class Meeting(models.Model):
    meet_id = models.AutoField(primary_key=True, unique=True)
    meet_owner = models.ForeignKey(
        Employee, 
        related_name='%(class)s_owner',
        on_delete=models.CASCADE
    )
    place = models.CharField(max_length=500)
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)
    attendies = models.ForeignKey(
        Employee, 
        related_name='%(class)s_attendies',
        on_delete=models.CASCADE
    )
    topics = models.ManyToManyField(Topic)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True, unique=True)
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    created = models.CharField(max_length=30)


class MeetingStatus(models.Model):
    meet_id = models.ForeignKey(
        Meeting, 
        related_name='%(class)s_meetings',
        on_delete=models.CASCADE
    )
    reviews = models.ForeignKey(
        Review,
        related_name='%(class)s_meetings',
        on_delete=models.CASCADE
    )
