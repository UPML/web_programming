# coding: utf-8
from django.db import models


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey('post.Post')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'комментарий'
        verbose_name_plural = u'комментарии'
