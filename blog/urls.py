from django.urls import path
from . import views #현재 폴더 - bolg에 있는 views.py를 사용할 수 있게 가져와라

urlpatterns = [
    path('<int:pk>/', views.single_post_page),#정수 형태의 pk 값이 붙는 url이라면 해당 함수에 정의된 대로 처리
    path('', views.PostList.as_view())
    # path('', views.index), #view의 index함수를 실행
]