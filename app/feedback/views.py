from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from feedback.serializers import FeedbackSerializer, OfferSerializer


class FeedbackViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = FeedbackSerializer(data={'book': request.data['book'], 'user': request.user.id, 'text': request.data['text']})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OfferViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = OfferSerializer(data={'offer': request.data['offer'], 'user': request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
