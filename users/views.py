from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
    """
    Class is used to get list of all the users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CurrentUser(generics.RetrieveAPIView):
    """
    Class is used to get current login user details.
    """

    def get(self, request):
        """
        Function is used to get current login user for testing purpose & return the details.
        :param request:request header with required info for get current login user info.
        :return:current login user.
        """
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
