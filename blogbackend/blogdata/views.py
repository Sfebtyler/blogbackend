from rest_framework import status
from rest_framework.decorators import list_route
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from blogdata.models import Post
from rest_framework import viewsets
from blogdata.serializers import UserSerializer, GroupSerializer, PostSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        return Response(status=400)

    @list_route(methods=['GET'], permission_classes=[])
    def current_user(self, request, *args, **kwargs):
        if self.request.user:
            return Response(UserSerializer(self.request.user, context={'request': request}).data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Not logged in!'}, status=status.HTTP_401_UNAUTHORIZED)

    @list_route(methods=['POST'], permission_classes=[])
    def create_user(self, request):
        UserSerializer.create_user(self, request)
        return Response(User)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-createdon')
    serializer_class = PostSerializer
    permission_classes = {}


    def list(self, request, *args, **kwargs):
        if request.method == 'GET':

            posts = self.get_queryset().filter(createdby=request.user)
            if posts:
                serializer = self.get_serializer(instance=posts, many=True)

                return Response(serializer.data)

        return Response([])







