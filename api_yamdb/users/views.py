from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from users.models import User
from users.paginators import UsersPaginator
from users.permissions import IsAdminUser
from users.serializers import (CustomUserSerializer, TokenSerializer,
                               UserSerializer, UsersSerializer)
from users.utils import send_confirmation_code


class SignupViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if isinstance(serializer.validated_data, dict):
            self.perform_create(serializer)
        send_confirmation_code(serializer.data['username'],
                               serializer.data['email'])
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK,
            headers=headers
        )


class TokenView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = TokenSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                serializer.validated_data,
                status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options',
                         'trace']
    permission_classes = (IsAdminUser,)
    lookup_field = 'username'
    pagination_class = UsersPaginator
    filter_backends = (SearchFilter,)
    search_fields = ('username',)


class CurrentUserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'patch', 'head', 'options', 'trace']

    def get_object(self):
        return self.request.user
