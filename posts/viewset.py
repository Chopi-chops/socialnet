from rest_framework import viewsets
from posts.models import *
from posts.serializers import *


class PostViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PostSerializer


class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class DislikeViewSet(viewsets.ModelViewSet):
    queryset = Dislike.objects.all()
    serializer_class = DislikeSerializer

