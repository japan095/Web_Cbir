from django.contrib import admin
from django.urls import path
from products import views
urlpatterns = [
    path('', views.addProduct, name="add-prod"),  
    path('edit-product/<str:pk>', views.editProduct, name="edit-prod"),
]