from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostList(ListView):
    model = Post #여러 post를 나열할 때 - CBV ListView를 사용할 것, model은 post다
    ordering = '-pk'

# def index(request):
#     posts = Post.objects.all().order_by('-pk') #모든 post 레코드를 가져와 posts에 저장 - all() 다 가져와라, order_by('-pk') 내림차순으로 가져와라
#
#     return render( #posts를 딕셔너리 형태로 추가
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) #괄호 안에 조건을 만족하는 post 레코드를 가져와라

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post, #가져온 레코드 하나를 html 페이지에 담아 렌더링
        }
    )
