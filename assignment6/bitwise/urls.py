from django.urls import path
from . import views

urlpatterns = [
    path('', views.input_view, name='input'),
    path('history/', views.history_view, name='history'),
]