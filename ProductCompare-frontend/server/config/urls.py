"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


urlpatterns = [
    path("admin/", admin.site.urls),
    # path("api/user/", include("accounts.urls")),
    path("api/ocr/", include("ImageConverters.urls")),
]
#
# schema_view = get_schema_view(
#     openapi.Info(
#         title='회원 관리',
#         default_version='v1',
#         description=
#         '''
#         register
#         회원가입(post)
#
#
#         auth
#         로그인(post/ get)
#         로그아웃(delete)
#
#         list
#         회원 정보(get)
#         is_authenticated 권한 필요
#
#         작성자 : ksb
#         ''',
#         terms_of_service='',
#         contact=openapi.Contact(name='이름', email='이메일'),
#         license=openapi.License(name='API 문서 이름')
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny,],
#     patterns=urlpatterns,
# )
#
# urlpatterns += [
#     path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]