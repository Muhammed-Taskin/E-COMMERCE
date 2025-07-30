from django.urls import path
from . import views

app_name = "commerce_app"

urlpatterns = [
    path("", views.homepage and views.products, name="homepage"),
    path("login/", views.log_in, name="login"),
    path("register/", views.register, name="register"),
    path("categories/",views.categories, name="categories"),
    path("products/", views.products, name="products"),
    path("product/<int:product_id>/", views.product_view, name= "product_view"),
    path("add_to_cart/<int:product_id>/", views.add_to_cart, name = "add_to_cart"),
    path("cart/<int:product_id>/", views.cart, name="cart"),
    path("cart/", views.cart, name = "cart_home" ),
    path("cart/incrase_qty/<int:product_id>/", views.increase_qty, name="increase_qty"),
    path("cart/decrease_qty/<int:product_id>/", views.decrease_qty, name="decrease_qty"),
    path("cart/remove_product/<int:product_id>/", views.remove_product, name="remove_product")  
]

