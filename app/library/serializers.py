from rest_framework import serializers

from feedback.serializers import FeedbackSerializer
from library.models import Book, Category, Image, Ownership, Reservation


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class ReservationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Reservation
        fields = '__all__'


class OwnershipSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Ownership
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    image = ImageSerializer()
    reservations = ReservationSerializer(many=True)
    feedbacks = FeedbackSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'
