from rest_framework import permissions, views
from rest_framework.response import Response

from core.serializers import UserSerializer


class UserViewSet(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
