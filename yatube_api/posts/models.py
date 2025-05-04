from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField('Текст публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Картинка', upload_to='posts/',
                              null=True, blank=True)
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        related_name='posts',
        null=True,
        blank=True
    )


class Group(models.Model):
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('Уникальный URL-адрес', unique=True)
    description = models.TextField('Описание группы')

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following'
    )
