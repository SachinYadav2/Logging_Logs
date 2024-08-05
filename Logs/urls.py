from django.shortcuts import render
from django.urls import path
from  Logs import views
app_name = "Logs"
urlpatterns = [
    path("" ,views.Home , name="Home"),

]