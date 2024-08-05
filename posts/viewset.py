from rest_framework import viewsets
from posts.models import Publication
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PostSerializer
