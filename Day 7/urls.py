from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name="Home"),
    path('about',views.aboutpageview,name="About"),
    path('contact',views.contactpageview,name="Contact"),
]
