from django.urls import path
from .import views

urlpatterns = [
    path('home',views.homepageview,name="home"), 
    path('about',views.aboutpageview,name='about'),
    path('contact',views.contactpageview,name='contact'),
    path('',views.myform,name='myform'),
    path('formprocess',views.process,name='process'),
    path('slist',views.studentlist.as_view(),name='s1'),
    path('elist',views.employeelist.as_view(),name='s2'),
]