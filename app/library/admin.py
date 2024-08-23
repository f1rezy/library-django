from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from feedback.admin import FeedbackInline
from library.models import Book, Image, Ownership, Reservation


class Image(TabularInline):
    model = Image
    fields = ('image',)


class ReservationInline(TabularInline):
    model = Reservation
    readonly_fields = ('user', 'created')


class OwnershipInline(TabularInline):
    model = Ownership
    readonly_fields = ('user', 'started')


@admin.register(Book)
class BookAdmin(ModelAdmin):
    list_display = (
        Book.title.field.name,
        Book.image_tmb,
    )
    search_fields = (
        Book.title.field.name,
    )
    inlines = (
        Image,
        ReservationInline,
        OwnershipInline,
        FeedbackInline,
    )


@admin.register(Reservation)
class ReservationAdmin(ModelAdmin):
    list_display = (
        Reservation.book.field.name,
        Reservation.user.field.name,
        Reservation.created.field.name,
    )
    readonly_fields = (
        Reservation.created.field.name,
    )


@admin.register(Ownership)
class OwnershipAdmin(ModelAdmin):
    list_display = (
        Ownership.book.field.name,
        Ownership.user.field.name,
        Ownership.started.field.name,
        Ownership.ended.field.name,
    )
    readonly_fields = (
        Ownership.started.field.name,
    )
