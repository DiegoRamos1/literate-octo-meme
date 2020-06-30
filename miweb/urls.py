from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('Origen',views.Origen,name="Origen"),
    path('Autocuidado',views.Autocuidado,name="Autocuidados"),
]