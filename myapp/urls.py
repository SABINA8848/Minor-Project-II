from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   
    path("", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("products/dress/", views.dress, name='dress'),
    path("products/skirts/", views.skirts, name='skirts'),
    path("products/pants/", views.pants, name='pants'),
    path("fav/", views.fav, name='fav'),
    path("cart/", views.cart, name='cart'),
    path("account/", views.account, name='account'),
    path("collection/", views.collection, name='collection'),
    path("product/", views.product, name='product'),
    path("winter/", views.winter, name='winter'),
    path('collection_pants/', views.collection_pants, name='collection_pants'),
    path('collection_shirts/', views.collection_shirts, name='collection_shirts'),
    path('login/',views.login,name='login'),
    path('finalpayment/', views.finalpayment, name='finalpayment'),
    path('success/', views.success, name='success'),
   
]
