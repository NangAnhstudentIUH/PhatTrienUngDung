from django.contrib import admin

# Register your models here.
from .models import Locaion, Item

admin.site.register(Locaion)
admin.site.register(Item)
