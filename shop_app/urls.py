from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.fun, name='fun'),
    path('<slug:c_slug>/',views.fun,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.ProductDetails,name='details'),
    path('search', views.searching, name='search')
    ]