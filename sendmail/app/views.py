from django.shortcuts import render
from django.views.generic import View
from .models import Car, Trailers
from .mixins import ObjectMixins
def index(request):
    return render(request, "index.html", )


# class CarsView(View):
#     def get(self, request):
#         car_object = Car.objects.all()
#         return render(request, "cars.html", {"cars": car_object})
    

# class TrailersView(View):
#     def get(self, request):
#         trailers_object = Trailers.objects.all()
#         return render(request, "trailers.html", {"trailers": trailers_object})

class CarsView(ObjectMixins, View):
    model = Car 
    template = "cars.html"

class TrailersView(ObjectMixins, View):
    model = Trailers 
    template = "trailers.html"


