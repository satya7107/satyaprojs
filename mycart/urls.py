from django.urls import path
from .import views as cviews

urlpatterns =[
    path('',cviews.cart,name="cart"),
    path('add_cart/<int:product_id>/',cviews.add_cart,name="add_cart"),
    path('remove_cart/<int:product_id>/',cviews.remove_cart,name="remove_cart"),
    path('remove_cart_item/<int:product_id>/',cviews.remove_cart_item,name="remove_cart_item"),

]