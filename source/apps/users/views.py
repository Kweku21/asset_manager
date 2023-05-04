from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet

from source.apps.users.serializer import UserSerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


user_view = UserViewSet.as_view({'get': 'list'})
