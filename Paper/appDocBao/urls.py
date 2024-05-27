"""
URL configuration for appDocBao project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from api.views import login, register, verify

from api.views import UserList
from api.views import UserViewSet
from api.views import homepage
from api.views import article
from api.views import search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='Login'),
    path('register/', register, name='register'),
    path('verify/', verify, name='verify'),

    # api users
    path('api/user/',  UserViewSet.as_view({'get': 'list_users'})),
    # api user update verify
    path('api/user/update/<int:pk>/', UserViewSet.as_view({'get': 'update_verify'})),
    # delete user
    path('api/user/delete/<int:pk>/', UserViewSet.as_view({'get': 'delete_user'})),
    # aproved all not verified
    path('api/user/aproved_all_not_verified/', UserViewSet.as_view({'get': 'aproved_all_not_verified'})),
    # unaproved all verified
    path('api/user/unaproved_all_verified/', UserViewSet.as_view({'get': 'unaproved_all_verified'})),
    # change role to admin
    path('api/user/change_role_admin/<int:pk>/', UserViewSet.as_view({'get': 'change_role_admin'})),
    # change role to author
    path('api/user/change_role_author/<int:pk>/', UserViewSet.as_view({'get': 'change_role_author'})),
    # change role to user
    path('api/user/change_role_user/<int:pk>/', UserViewSet.as_view({'get': 'change_role_user'})),    
    # homepage
    path('api/homepage/', homepage, name='homepage'),
    # article with id
    path('api/article/<int:id>/', article, name='article'),
    # search
    path('api/search/<str:keyword>/', search, name='search'),
]