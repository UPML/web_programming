# coding: utf-8
from django.db import models


class Blog(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'блог'
        verbose_name_plural = u'блоги'
