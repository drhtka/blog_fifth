# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    """Посты блога"""
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        db_table = 'bp'

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=100,)
    text = models.TextField('Текст статьи',)
    date_pub = models.DateTimeField('Дата публикации',)
    order_to_sent = models.BooleanField('Разослать уведомления?', default=False)
    sent_out = models.BooleanField('Уведомления разосланы', default=False)

    def __str__(self):
        return self.title

class PersonalBlog(models.Model):
    """Модель хранения данных о публикациях, подписках и подписчиках"""
    class Meta:
        verbose_name = 'Пост пользователя'
        verbose_name_plural = 'Посты пользователей'

    author = models.ForeignKey(User, related_name='author_blog', on_delete=models.CASCADE)
    posts = models.ManyToManyField(BlogPost, verbose_name='Посты', blank=True, related_name='posts')
    feeds = models.ManyToManyField(User, verbose_name='Подписки', blank=True, related_name='feeds')
    followers = models.ManyToManyField(User, verbose_name='Подписчики', blank=True, related_name='followes')
    noted = models.ManyToManyField(BlogPost, blank=True, verbose_name='Прочитано', related_name='noted')


    def __str__(self):
        return self.author.username
