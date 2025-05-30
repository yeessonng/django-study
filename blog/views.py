from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-pk') #모든 post 레코드를 가져와 posts에 저장 - all() 다 가져와라, order_by('-pk') 내림차순으로 가져와라

    return render( #posts를 딕셔너리 형태로 추가
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
