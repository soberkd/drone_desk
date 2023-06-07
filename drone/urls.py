from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),
    path('another/', views.another_view, name='another_view'),
]
