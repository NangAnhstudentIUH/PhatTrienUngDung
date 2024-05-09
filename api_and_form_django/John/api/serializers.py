from rest_framework import serializers
from .models import Item, Locaion

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('__all__')


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locaion
        fields = ('__all__')