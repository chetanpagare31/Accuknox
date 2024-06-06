

from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email= validated_data['email'].lower(),
            password=validated_data['password']
        )
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only = True)

class SearchUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = serializers.StringRelatedField(source='from_user.username')
    # to_user = serializers.StringRelatedField(source='to_user.username')

    class Meta:
        model = FriendRequest
        fields = ['id','from_user','status','timestamp']
        read_only_fields = ['from_user','status','timestamp']