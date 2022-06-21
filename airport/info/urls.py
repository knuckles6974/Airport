from django.contrib import admin
from .views         import AirportInfoView
from django.urls import path

urlpatterns = [
    path('', AirportInfoView.as_view()),

]