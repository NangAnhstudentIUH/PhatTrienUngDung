from django.urls import path
from .views import api_news
from .views import opennew
urlpatterns = [

    path('apinews/', api_news, name='api_news'),
]
