from django.urls import path
from writer import views

urlpatterns = [
    path('', views.writer),
]

