
from unicodedata import category
from unittest.util import _MAX_LENGTH
from venv import create
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    CATEGORY_CHOICE =[
        ('1', '일반'),
        ('2', '계정'),
        ('3', '기타'),
    ]
    image = models.CharField(verbose_name='질문제목', max_length=80)
    content = models.TextField(verbose_name='질문')
    category = models.DateTimeField(verbose_name='카테고리', max_length=2, choices=CATEGORY_CHOICE)
    
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    created_at = models.DateTimeField(verbose_name='최종수정일시', auto_now_add=True)
    created_at = models.ForeignKey(to =User, on_delete=models.CASCADE, related_name= 'faq_created_by')
    created_at = models.ForeignKey(to= User, on_delete=models.CASCADE, related_name='faq_updated_by')