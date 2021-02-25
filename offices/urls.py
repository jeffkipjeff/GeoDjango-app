from django.urls import path
from offices import views

urlpatterns = [
    path('', views.Home.as_view()),
]
