from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^\Z', views.SignIn.as_view(), name='signin'),
    url(r'^home/', views.Home.as_view(), name='home'),
    url(r'^signin/', views.SignIn.as_view(), name='signin'),
    url(r'^signup/', views.SignUp.as_view(), name='signup'),
    url(r'^data/', views.GetData.as_view(), name='data'),

]
