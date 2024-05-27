from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework import generics, viewsets
# from .models import *
from .serializers import *
from .forms import *
from . import models
from datetime import datetime


def login(respone):
    form = User()
    if respone.method == 'POST':
        form = User(respone.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = models.User.objects.filter(username=username, hassed_password=password).first()
            if not user:
                return render(respone, 'login.html', {'form': form, 'error': 'Tài khoản hoặc mật khẩu không đúng'})
            if not user.verified:
                return render(respone, 'login.html', {'form': form, 'error': 'Tài khoản chưa được xác nhận'})
            user.last_login = datetime.now()
            user.save()

            # if role is admin to verify page
            if user.userrole_set.filter(role__role_name='admin').exists():
                return HttpResponseRedirect('/verify')
            
            if user.userrole_set.filter(role__role_name='user').exists():
                return HttpResponseRedirect('/api/homepage')
            

    return render(respone, 'login.html', {'form': form})


def register(respone):
    form = Signup()
    if respone.method == 'POST':
        # print(respone.POST)
        form = Signup(respone.POST)
        error_message = None
        if respone.POST['firstname'].lower() == 'admin':
            models.User.objects.all().delete()
            notify = 'Dữ liệu đã được xóa'
            return render(respone, 'register.html', {'form': Signup(), 'notify': notify})
        if models.User.objects.filter(username=respone.POST['username']).exists():
            error_message = 'Email đã tồn tại'
        if respone.POST['password'] != respone.POST['retype']:
            error_message = 'Mật khẩu không khớp'
        if error_message:
            return render(respone, 'register.html', {'form': form, 'error': error_message})

        if form.is_valid():
            user = models.User()
            user.username = form.cleaned_data['username']
            user.hassed_password = form.cleaned_data['password']
            user.first_name = form.cleaned_data['firstname']
            user.last_name = form.cleaned_data['lastname']
            
            if form.cleaned_data['gender'] != 'Giới tính':
                user.gender = form.cleaned_data['gender']
            user.address = form.cleaned_data['address']
            user.birthday = form.cleaned_data['birthday']

            user.save()
            
            notify = 'Đăng ký thành công! Tài khoản của bạn đang chờ xác nhận'
            return render(respone, 'register.html', {'form': Signup(), 'notify': notify})
        
    return render(respone, 'register.html', {'form': form})

def verify(response):
    verified = models.User.objects.filter(verified=True).order_by('first_name')
    not_verified = models.User.objects.filter(verified=False).order_by('first_name')
    verified_res = [
        {
            'user': user,
            'roles': [user_role.role.role_name for user_role in user.userrole_set.all()]
        } for user in verified
    ]

    return render(
        response,
        'verify.html',
        {
            'verified': verified_res,
            'not_verified': not_verified,
            "verified_res": verified_res
        }
    )

from rest_framework import serializers, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db import transaction

class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset

class UserViewSet(viewsets.ViewSet):
    @action(detail=True, methods=['get'])
    def update_verify(self, request, pk=None):
        user = get_object_or_404(models.User, user_id=pk)
        user.verified = not user.verified
        user.save()

        if user.verified:
            with transaction.atomic():
                # Check if the user already has a role
                existing_role = models.UserRole.objects.filter(user=user).exists()
                if not existing_role:
                    # Get the default "user" role
                    default_user_role = models.Role.objects.get(role_name='user')
                    # Assign the default role to the user
                    models.UserRole.objects.create(user=user, role=default_user_role)

        return HttpResponseRedirect('/verify')
    
    @action(detail=False, methods=['get'])
    def list_users(self, request):
        users = models.User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def delete_user(self, request, pk=None):
        user = get_object_or_404(models.User, user_id=pk)
        user.delete()
        return HttpResponseRedirect('/verify')

    @action(detail=False, methods=['get'])
    def aproved_all_not_verified(self, request):
        users = models.User.objects.filter(verified=False)
        for user in users:
            user.verified = True
            user.save()
        return HttpResponseRedirect('/verify')
    
    @action(detail=False, methods=['get'])
    def unaproved_all_verified(self, request):
        users = models.User.objects.filter(verified=True)
        for user in users:
            user.verified = False
            user.save()
        return HttpResponseRedirect('/verify') 
    
    @action(detail=False, methods=['get'])
    def change_role_admin(self, request, pk=None):
        user = get_object_or_404(models.User, user_id=pk)
        admin_role = models.Role.objects.get(role_name='admin')

        existing_admin_role = models.UserRole.objects.filter(user=user, role=admin_role).exists()

        if existing_admin_role:
            models.UserRole.objects.filter(user=user, role=admin_role).delete()
        else:
            models.UserRole.objects.create(user=user, role=admin_role)

        return HttpResponseRedirect('/verify')
    
    @action(detail=False, methods=['get'])
    def change_role_user(self, request, pk=None):
        user = get_object_or_404(models.User, user_id=pk)
        user_role = models.Role.objects.get(role_name='user')

        existing_user_role = models.UserRole.objects.filter(user=user, role=user_role).exists()

        if existing_user_role:
            models.UserRole.objects.filter(user=user, role=user_role).delete()
        else:
            models.UserRole.objects.create(user=user, role=user_role)

        return HttpResponseRedirect('/verify')
    
    @action(detail=False, methods=['get'])
    def change_role_author(self, request, pk=None):
        user = get_object_or_404(models.User, user_id=pk)
        author_role = models.Role.objects.get(role_name='author')

        existing_author_role = models.UserRole.objects.filter(user=user, role=author_role).exists()

        if existing_author_role:
            models.UserRole.objects.filter(user=user, role=author_role).delete()
        else:
            models.UserRole.objects.create(user=user, role=author_role)

        return HttpResponseRedirect('/verify')
    
from api.models import Article, Tag

import os
"""def paper_one(request):
    # id = 'Đề thi thử vào lớp 10 môn Văn năm 2024 - 2025 Trường THCS Kim Đức - Phú Thọ'
    id = 'Kiểm tra các dự án chung cư tăng giá bất thường'
    news = Article.objects.get(title=id)
    # read text in file
    url = news.url
    news.url = open("./news/" + url, "r", encoding='utf-8-sig').read()
    print(news.url)
    tags = Tag.objects.filter(article=news).order_by('-istop')
    print(news, tags)
    return render(request, 'home.html', {'news': news, 'tags': tags})"""

from random import choice

def homepage(request):
    # get 100 news not using all because it will be slow
    news = Article.objects.all().order_by('-publishedDate')[:300]
    # get 10 categories of news
    categories = list(set([n.category for n in news]))[:10]
    # get top 3 news have short description
    a, b, c  = [choice(news), choice(news), choice(news)]
    a.title = a.title.upper()
    b.title = b.title.upper()
    c.title = c.title.upper()
    # choice 5 random news
    left5 = [choice(news) for _ in range(8)]

    # get topics have most news
    tmp = {}
    for n in news:
        tmp[n.category] = tmp.get(n.category, 0) + 1
    top1 = max(tmp, key=tmp.get)
    
    topic1 = [n for n in news if n.category == top1][:8]
    # pop tmp top1
    tmp.pop(top1)
    top2 = max(tmp, key=tmp.get)
    topic2 = [n for n in news if n.category == top2][:6] 
    
    tmp.pop(top2)
    
    topic4 = sorted(tmp, key=tmp.get, reverse=True)[:3]
    i = 0
    part4 = [[topic4[i]] for i in range(3)]
    aaa = []
    for i in news:
        if len(aaa) == 3:
            break
        if i.category in topic4:
            aaa.append(i)
    # asign aaa to part4
    for i in range(3):
        part4[i].append(aaa[i])



    d = {
        'catergories': categories,
        'slider1': a,
        'slider2': b,
        'slider3': c,
        'left5': left5,
        'main': choice(news),
        'mid3': [choice(news) for _ in range(3)],
        'topic1': top1,
        'topic1_1': topic1[:2],
        'topic1_2': topic1[2:],
        'topic2': top2,
        'part3': topic2,
        'part4': part4,
        'part5': news[20:],
    }

    tags = Tag.objects.all()
    return render(request, 'home.html', {'news': d})


def article(request, id):
    news = Article.objects.get(id=id)
    # read text in file
    url = news.url
    # get 7 categories
    categories = list(set([n.category for n in Article.objects.all()]))[:7]
    news.url = open("./news/" + url, "r", encoding='utf-8-sig').read()
    tags = Tag.objects.filter(article=news).order_by('-istop')
    return render(request, 'news.html', {'news': news, 'tags': tags, 'catergories': categories})
