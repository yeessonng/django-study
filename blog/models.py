from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField() #문자 길이 제한 x

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) #이미지를 저장할 폴더의 경로 규칙 지정
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/' #문자열 포맷팅f