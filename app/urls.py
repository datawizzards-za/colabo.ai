from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^\Z', views.Home.as_view(), name='home'),
    url(r'^app/', views.Home.as_view(), name='home'),
]
