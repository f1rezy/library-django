from django.contrib.auth.models import User
from django.db import models

from core.models import Model
from library.models import Book


class Feedback(Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name='книга',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name='пользователь',
    )
    text = models.TextField(
        'текстовое поле',
    )
    created_on = models.DateTimeField(
        'дата и время создания',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
        default_related_name = 'feedbacks'

    def __str__(self):
        return self.text[:15]


class Offer(Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='offers',
        verbose_name='пользователь',
    )
    offer = models.CharField(
        'предложение',
        max_length=100,
        null=True,
        blank=True,
    )
    created_on = models.DateTimeField(
        'дата и время предложения',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        verbose_name = 'предложение'
        verbose_name_plural = 'предложения'
        default_related_name = 'offers'

    def __str__(self):
        return self.offer[:15]
