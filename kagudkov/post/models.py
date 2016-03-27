# coding: utf-8
from django.db import models
from datetime import datetime
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    blog = models.ForeignKey('blog.Blog', related_name='post')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    moderator = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='published_posts')

    class Meta:
        verbose_name = u'пост'
        verbose_name_plural = u'посты'

