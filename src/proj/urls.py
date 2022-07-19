"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from handbook import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view()),
    path('author_list/', views.AuthorList.as_view()),
    path('author/<int:pk>/', views.AuthorDetail.as_view()),
    path('author_add/', views.AuthorAdd.as_view()),
    path('author_delete/<int:pk>/', views.AuthorDelete.as_view()),
    path('author_edit/<int:pk>/', views.AuthorEdit.as_view()),
    path('serie_list/', views.SerieList.as_view()),
    path('serie/<int:pk>/', views.SerieDetail.as_view()),
    path('serie_add/', views.SerieAdd.as_view()),
    path('serie_delete/<int:pk>/', views.SerieDelete.as_view()),
    path('serie_edit/<int:pk>/', views.SerieEdit.as_view()),
    path('genre_list/', views.GenreList.as_view()),
    path('genre/<int:pk>/', views.GenreDetail.as_view()),
    path('genre_add/', views.GenreAdd.as_view()),
    path('genre_delete/<int:pk>/', views.GenreDelete.as_view()),
    path('genre_edit/<int:pk>/', views.GenreEdit.as_view()),
    path('publisher_list/', views.PublisherList.as_view()),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view()),
    path('publisher_add/', views.PublisherAdd.as_view()),
    path('publisher_delete/<int:pk>/', views.PublisherDelete.as_view()),
    path('publisher_edit/<int:pk>/', views.PublisherEdit.as_view()),
    path('book_list/', views.BookList.as_view()),
    path('book/<int:pk>/', views.BookDetail.as_view()),
    path('book_add/', views.BookAdd.as_view()),
    path('book_delete/<int:pk>/', views.BookDelete.as_view()),
    path('book_edit/<int:pk>/', views.BookEdit.as_view()),
]
