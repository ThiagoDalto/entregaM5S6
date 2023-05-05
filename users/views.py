from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView, Request, Response, status
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .permissions import IsSuperuser
import ipdb

from .models import User
from .serializers import UserSerializer


class UserView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperuser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # def perform_create(self, serializer):
    #     """
    #     Registro de usuários
    #     """
    #     serializer.save()

    # def get_queryset(self):
    #     """
    #     Listagem de usuários
    #     """
    #     ipdb.set_trace()
    #     user_id = self.kwargs["pk"]

    #     user_obj = get_object_or_404(User, pk=user_id)
    #     self.check_object_permissions(self.request, user_obj)
    #     users = User.objects.filter(user=user_obj)

    #     return users
