from django.urls import path
# 현재 폴더에 있는 views.py를 사용할 수 있게 가져와라 
from . import views 

urlpatterns = [
    path('',views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]
