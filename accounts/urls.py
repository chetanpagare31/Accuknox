
from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('signin/', LoginUserView.as_view(), name='signin'),
    path('get_users/', UserView.as_view(), name='get_users'),

    path('refresh/',TokenRefreshView.as_view(), name='refresh-token'),
    path('search_users/', SearchUserView.as_view(), name='search_users'),
    path('friend_request/', FriendRequestView.as_view(), name='friend-request'),
    path('list_friends/', ListFriendsView.as_view(), name='list_friends'),
    path('list_pending_request/', ListPendingRequestView.as_view(), name='list_pending_request'),
    
]
