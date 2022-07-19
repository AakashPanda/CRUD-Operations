from django import views
from django.urls import path 

from . import views


urlpatterns = [
    path('', views.home, name="hompage"),
    path('add/',views.add,name="add"),
    path('edit/',views.Edit,name="edit"),
    path('update/<str:id>',views.Update,name="update"),
    path('delete/<str:id>',views.Delete,name="delete"),
]
