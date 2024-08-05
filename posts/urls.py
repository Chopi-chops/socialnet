from django.urls import path, include
from posts.views import *
from rest_framework import routers
from posts.viewset import *


post_router = routers.DefaultRouter()
post_router.register("viewset", PostViewSet)


urlpatterns = [
    path("list/", PostsList.as_view(), name="posts-list"),
    path('info/<int:pk>/', PostInfo.as_view()),
    path('create/', PostCreate.as_view(), name='post-create'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post-update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post-delete'),

    path('v3/', include(post_router.urls))
]
