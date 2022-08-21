from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path('book_list/', views.BookList.as_view(), name="book-list"),
    path('book/<int:pk>/', views.BookDetail.as_view(), name="book-view"),
    path('book_add/', views.BookAdd.as_view(), name="book-add"),
    path('book_delete/<int:pk>/', views.BookDelete.as_view(), name="book-delete"),
    path('book_edit/<int:pk>/', views.BookEdit.as_view(), name="book-edit"),
    path('book_search/', views.BookSearch.as_view(), name="book-search"),
]