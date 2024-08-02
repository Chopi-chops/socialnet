from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Publication
from posts.serializers import PostSerializer


class PostsList(APIView):
    def get(self, request, *args, **kwargs):
        posts_list = Publication.objects.all()
        serializer = PostSerializer(instance=posts_list, many=True)
        return Response(data=serializer.data)


class PostInfo(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        post_object = Publication.objects.get(pk=pk)
        serializer = PostSerializer(instance=post_object)
        return Response(data=serializer.data)
