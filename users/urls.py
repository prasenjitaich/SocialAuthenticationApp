from django.urls import path
from .views import UserList, CurrentUser

urlpatterns = [
    path('all-users/', UserList.as_view()),
    path('current-user/', CurrentUser.as_view())
]
