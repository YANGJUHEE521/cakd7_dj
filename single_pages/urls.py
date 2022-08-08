from django.urls import path
from . import views

urlpatterns = [
    path('about_me/', views.about_me), #자기 소개 페이지
    path('', views.landing), #대문 페이지
]