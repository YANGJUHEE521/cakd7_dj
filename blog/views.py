from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    ordering = '-pk'  #최신 글부터 맨 위에 배치 
    template_name= 'blog/index.html'

class PostDetail(DetailView):
    model = Post



# Create your views here.
