from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cars",views.CarsView.as_view(), name="cars"),
    path("trailers",views.TrailersView.as_view(),name="trailers" ),
]
