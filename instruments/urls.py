from django.urls import path
from . import views

urlpatterns = [
    path('', views.instrument_list, name='instrument_list'),
]
