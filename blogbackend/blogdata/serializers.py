from django.contrib.auth.models import User, Group
from blogdata.models import Post
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create_user(self, request):
        user = User(
            email=request.data['email'],
            username=request.data['username']
        )
        user.set_password(request.data['password'])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'posttext', 'createdby', 'createdon', 'postimage')
