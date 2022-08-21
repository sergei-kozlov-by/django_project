from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path('cart/', views.AddToCart.as_view(), name="add-to-cart"),
    path('delete_from_cart/<int:pk>/', views.DeleteFromCart.as_view(), name="delete-from-cart"),
    path('update_cart/', views.UpdateCart.as_view(), name="update-cart"),
    path('order_list/', views.OrderList.as_view(), name="order-list"),
    path('order_view/<int:pk>/', views.OrderView.as_view(), name="order-view"),
    path('order_edit/<int:pk>/', views.OrderEdit.as_view(), name="order-edit"),
    path('order_delete/<int:pk>/', views.OrderDelete.as_view(), name="order-delete"),
]