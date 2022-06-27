from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logout, name='logout'),
    path("profile", views.profile, name='proile'),
    path("shop", views.shop, name='shop'),
    path("checkout", views.checkout, name='checkout'),
    path("products/<int:myid>", views.productView, name='productView'),
    path("tracker", views.shop, name='tracker'),
]