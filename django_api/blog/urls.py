from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('hew',views.second_home,name='new-home'),
]

