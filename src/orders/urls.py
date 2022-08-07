from django.urls import path
from . import views
app_name = "orders"


urlpatterns = [
    path('add-to-cart/', views.AddToCart.as_view(), name="add-to-cart"),
]