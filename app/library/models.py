from django.contrib.auth.models import User
from django.db import models
from django.utils.safestring import mark_safe
from sorl.thumbnail import get_thumbnail

from core.models import Model


def item_directory_path(instance, filename):
    return f'library/{instance.book.id}/{filename}'


class Category(Model):
    name = models.CharField(
        'название',
        max_length=150,
        help_text='max 150 символов',
        unique=True,
    )

    class Meta:
        ordering = ('name', 'id')
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Book(Model):
    title = models.CharField(
        'название',
        max_length=150,
        help_text='max 150 символов',
        unique=True,
    )
    author = models.CharField(
        'автор',
        max_length=100,
        help_text='max 100 символов',
    )
    description = models.CharField(
        'описание',
        max_length=300,
        help_text='max 300 символов',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='категория',
        help_text='Выберите категорию',
        related_name='books',
    )

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'
        default_related_name = 'books'

    def __str__(self):
        return self.title

    def image_tmb(self):
        if self.image:
            return mark_safe(
                f"<img src='{self.image.get_image_300x300.url}'>",
            )
        return 'Нет изображения'

    image_tmb.short_description = 'изображение'
    image_tmb.allow_tags = True


class Image(Model):
    image = models.ImageField(
        'изображение',
        upload_to=item_directory_path,
        default=None,
    )
    book = models.OneToOneField(
        Book,
        on_delete=models.CASCADE,
        related_name='image',
    )

    @property
    def get_image_300x300(self):
        return get_thumbnail(self.image, '300x300', crop='center', quality=51)

    def __str__(self):
        return str(self.book.title)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'фото'


class Reservation(Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reservations',
        verbose_name='книга',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reservations',
        verbose_name='пользователь',
    )
    created = models.DateTimeField(
        'время бронирования',
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ('created', 'id')
        verbose_name = 'бронирование'
        verbose_name_plural = 'бронирования'
        default_related_name = 'reservations'
        unique_together = ('book', 'user')

    def __str__(self):
        return str(self.id)


class Ownership(Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='ownerships',
        verbose_name='книга',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='ownerships',
        verbose_name='пользователь',
    )
    started = models.DateTimeField(
        'начало владения',
        auto_now_add=True,
        editable=False,
    )
    ended = models.DateTimeField(
        'конец владения',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = 'владение'
        verbose_name_plural = 'владения'
        default_related_name = 'ownerships'

    def __str__(self):
        return str(self.id)
