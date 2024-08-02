from django.urls import path
from posts.views import *


urlpatterns = [
    path("list/", PostsList.as_view(), name="posts-list"),
    path('info/<int:pk>/', PostInfo.as_view()),
]
