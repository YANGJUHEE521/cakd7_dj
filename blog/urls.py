from django.urls import path
# 현재 폴더에 있는 views.py를 사용할 수 있게 가져와라 
from . import views 

urlpatterns = [
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/', views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('<int:pk>/new_comment/', views.new_comment),
    path('',views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
]
