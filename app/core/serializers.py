from django.contrib.auth.models import User
from rest_framework import serializers

from feedback.serializers import FeedbackSerializer, OfferSerializer
from library.serializers import OwnershipSerializer, ReservationSerializer


class UserSerializer(serializers.ModelSerializer):
    reservations = ReservationSerializer(many=True)
    ownerships = OwnershipSerializer(many=True)
    feedbacks = FeedbackSerializer(many=True)
    offers = OfferSerializer(many=True)

    class Meta:
        model = User
        fields = ['username', 'reservations', 'ownerships', 'feedbacks', 'offers']
