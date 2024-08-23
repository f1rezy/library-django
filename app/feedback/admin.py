from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from feedback.models import Feedback, Offer


class FeedbackInline(TabularInline):
    model = Feedback
    readonly_fields = ('user', 'text', 'created_on')


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        Feedback.book.field.name,
        Feedback.user.field.name,
        Feedback.created_on.field.name,
    )


@admin.register(Offer)
class OfferAdmin(ModelAdmin):
    list_display = (
        Offer.user.field.name,
        Feedback.created_on.field.name,
    )
