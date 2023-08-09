from django.urls import path, include

from accounts.views import RegisterAPIView, AuthAPIView, UserViewSet
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", RegisterAPIView.as_view()),
    path("auth/", AuthAPIView.as_view()),
    path("auth/refresh/", TokenRefreshView.as_view()),
]