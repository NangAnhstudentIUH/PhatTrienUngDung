from rest_framework import generics
from .models import Item, Locaion
from .serializers import ItemSerializer, LocationSerializer

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import CreateNewList, CreateLocation


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if not Locaion:
            queryset = queryset.filter(itemLocation=location)

        return queryset
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Locaion.objects.all()
class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Locaion.objects.all()


def create(response):
    if response.method == "POST":
        form = CreateLocation(response.POST)
        if form.is_valid():
            n = form.cleaned_data["locationName"]
            t = Locaion(locationName=n)
            t.save()
        return HttpResponseRedirect(f"/api/location/")
    else:
        form = CreateLocation()
    return render(response, "create.html", {"form": form})