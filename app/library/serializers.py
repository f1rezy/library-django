from rest_framework import serializers

from feedback.serializers import FeedbackSerializer
from library.models import Book, Image, Ownership, Reservation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class ReservationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'


class OwnershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ownership
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    reservations = ReservationSerializer(many=True)
    feedbacks = FeedbackSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'
