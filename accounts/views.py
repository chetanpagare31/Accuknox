from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.pagination import PageNumberPagination
from .models import *
from django.utils import timezone
from datetime import timedelta

class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset,many=True)
        return Response(serializer.data)


class RegisterUserView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
    def post(self,request,*args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email'].lower()
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    refresh = RefreshToken.for_user(user)
                    response_data = {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user': UserSerializer(user).data
                    }
                    return Response(response_data,status=status.HTTP_200_OK)
                else:
                    return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({'error':'Invalid email'},status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class SearchUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    class Pagination(PageNumberPagination):
        page_size = 10

    def get(self,request):
        keyword = request.query_params.get('q','').lower()
        if '@' in keyword:
            users = User.objects.filter(email__iexact=keyword)
        else:
            users =User.objects.filter(username__icontains=keyword)
        
        paginator = self.Pagination()
        result = paginator.paginate_queryset(users, request)
        serializer = SearchUserSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)





class FriendRequestView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request,*args,**kwargs):
        to_username = request.data.get('to_user') 
        try:
            to_user = User.objects.get(username=to_username)
        except User.DoesNotExist:
            return Response({'error': 'User with username {} not found.'.format(to_username)}, status=status.HTTP_404_NOT_FOUND)
    

        if request.user.sent_request.filter(to_user=to_user, status='pending').exists():
            return Response({'error':'You have already sent a friend request to this user'},status=status.HTTP_400_BAD_REQUEST)
        
        one_minute_ago = timezone.now() - timedelta(minutes=1)
        pending_requests_count = request.user.sent_request.filter(status='pending', timestamp__gte=one_minute_ago).count()
        
        if pending_requests_count >= 3:
            return Response({'error': 'You cannot send more than 3 friend requests within a minute.'}, status=status.HTTP_400_BAD_REQUEST)
    
        friend_request, created = FriendRequest.objects.get_or_create(from_user = request.user, to_user=to_user)

        if not created:
            return Response({'error':'Friend Request alreaddy exists'},status=status.HTTP_400_BAD_REQUEST)
        
        return Response(FriendRequestSerializer(friend_request).data, status=status.HTTP_201_CREATED)


    def patch(self, request, *args, **kwargs):
        from_username = request.data.get('from_user')
        status_detail = request.data.get('status')

        if status_detail not in ['accepted','rejected']:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            from_user = User.objects.get(username=from_username)
            friend_request = FriendRequest.objects.get(from_user=from_user, to_user=request.user, status='pending')
            friend_request.status = status_detail
            friend_request.save()
            return Response(FriendRequestSerializer(friend_request).data)
        
        except FriendRequest.DoesNotExist:
            return Response({'error': 'Friend request not found.'}, status=status.HTTP_404_NOT_FOUND)
        except User.DoesNotExist:
            return Response({'error': 'Friend request for this user not found.'}, status=status.HTTP_404_NOT_FOUND)

class ListFriendsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        friends = User.objects.filter(sent_request__to_user=request.user,sent_request__status='accepted'
        ) | User.objects.filter(received_request__to_user=request.user,received_request__status='accepted')
        friends = friends.distinct().exclude(id=request.user.id)
        serializer = SearchUserSerializer(friends,many=True)
        return Response(serializer.data)

class ListPendingRequestView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        pending_requests = FriendRequest.objects.filter(to_user=request.user,status='pending')
        serializer =FriendRequestSerializer(pending_requests,many=True)
        return Response(serializer.data)