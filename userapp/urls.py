from django.urls import path, include
from userapp.views import *
from rest_framework import routers
from userapp.viewset import *


user_router = routers.DefaultRouter()
user_router.register("viewset", UserViewSet)


urlpatterns = [
    path("list/", UserList.as_view(), name="user-list"),
    path('info/<int:pk>/', UserInfo.as_view()),

    path('v3/', include(user_router.urls))
]
