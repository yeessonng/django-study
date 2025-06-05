from django.db import models
from django.contrib.auth.models import User #장고에서 기본적으로 제공하는 모델
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField() #문자 길이 제한 x

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #이미지를 저장할 폴더의 경로 규칙 지정
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE) #User를 사용해 author 필드 구성 / 이 post 작성자가 db에서 삭제되었을 때 이 포스트도 같이 삭제한다.

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/' #문자열 포맷팅f

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self): #확장자 찾기
        return self.get_file_name().split('.')[-1] #-1은 마지막 요소 ex) jpg

