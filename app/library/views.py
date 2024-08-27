from http import HTTPMethod

from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from library.models import Book
from library.serializers import BookSerializer, ReservationSerializer


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=[HTTPMethod.GET],
            url_path='search')
    def search_books(self, request):
        if request.query_params.get('search_field') is None or request.query_params.get('search_field') == '':
            return Response([])

        books = Book.objects.filter(title__icontains=request.query_params.get('search_field')) | Book.objects.filter(author__icontains=request.query_params.get('search_field'))

        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)


class ReservationViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = ReservationSerializer(data={'book': request.data['book'], 'user': request.user.id})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
