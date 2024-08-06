from django.urls import path, include
from posts.views import *
from rest_framework import routers
from posts.viewset import *


post_router = routers.DefaultRouter()
post_router.register("viewset", PostViewSet)
like_router = routers.DefaultRouter()
like_router.register("viewset", LikeViewSet)
dislike_router = routers.DefaultRouter()
dislike_router.register("viewset", DislikeViewSet)

urlpatterns = [
    path("list/", PostsList.as_view(), name="posts-list"),
    path('info/<int:pk>/', PostInfo.as_view()),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),

    path('v3/', include(post_router.urls)),
    path('v4/', include(like_router.urls)),
    path('v5/', include(dislike_router.urls)),
]
