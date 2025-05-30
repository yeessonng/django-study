from django.urls import path
from . import views #현재 폴더 - bolg에 있는 views.py를 사용할 수 있게 가져와라

urlpatterns = [
    path('', views.index), #view의 index함수를 실행
]