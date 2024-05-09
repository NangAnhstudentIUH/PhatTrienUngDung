from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import NewsArticle

# Create your views here.
def index(request, search=""):
    search = '/apinews/' + search
    return render(request, 'index.html', {'search': search})

def opennew(request):
    return render(request, 'paper.html')

def api_news(request):
    news = sorted(NewsArticle.objects.all(), key=lambda x:float(x.date), reverse=True)
    response_data = dict()
    
    for idx, n in enumerate(news):
        title, description, date, url, redirect_url, thumb, thumb_l, publisher = n.title, n.description, n.date, n.url, n.redirect_url, n.thumb, n.thumb_l, n.publisher
        response_data['news'+str(idx)] = {
            'title': title,
            'description': description,
            'date': date,
            'url': url,
            'redirect_url': redirect_url,
            'thumb': thumb,
            'thumb_l': thumb_l,
            'publisher': publisher
        }
    return JsonResponse(response_data)

import re
def api(request, text):
    news = sorted(NewsArticle.objects.all(), key=lambda x:float(x.date), reverse=True)
    response_data = dict()
    i = 0
    for idx, n in enumerate(news):
        title, description, date, url, redirect_url, thumb, thumb_l, publisher = n.title, n.description, n.date, n.url, n.redirect_url, n.thumb, n.thumb_l, n.publisher
        if re.search(text.lower(), title.lower()) or re.search(text.lower(), description.lower()):
            response_data['news'+str(i)] = {
                'title': title,
                'description': description,
                'date': date,
                'url': url,
                'redirect_url': redirect_url,
                'thumb': thumb,
                'thumb_l': thumb_l,
                'publisher': publisher
            }
            i += 1
    return JsonResponse(response_data)


def search(request):
    print(request.method)
    if request.method != 'GET':
        return HttpResponseRedirect(reverse('index'))
    
    text = request.GET['search']
    return index(request, text)