from django.conf.urls import url
import views

urlpatterns = [
    url(r'^\Z', views.Home.as_view(), name='name'),
]