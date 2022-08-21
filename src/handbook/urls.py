from django.urls import path
from . import views

app_name = "hb"

urlpatterns = [
    path('author_list/', views.AuthorList.as_view(), name="author-list"),
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name="author-view"),
    path('author_add/', views.AuthorAdd.as_view(), name="author-add"),
    path('author_delete/<int:pk>/', views.AuthorDelete.as_view(), name="author-delete"),
    path('author_edit/<int:pk>/', views.AuthorEdit.as_view(), name="author-edit"),
    path('serie_list/', views.SerieList.as_view(), name="serie-list"),
    path('serie/<int:pk>/', views.SerieDetail.as_view(), name="serie-view"),
    path('serie_add/', views.SerieAdd.as_view(), name="serie-add"),
    path('serie_delete/<int:pk>/', views.SerieDelete.as_view(), name="serie-delete"),
    path('serie_edit/<int:pk>/', views.SerieEdit.as_view(), name="serie-edit"),
    path('genre_list/', views.GenreList.as_view(), name="genre-list"),
    path('genre/<int:pk>/', views.GenreDetail.as_view(), name="genre-view"),
    path('genre_add/', views.GenreAdd.as_view(), name="genre-add"),
    path('genre_delete/<int:pk>/', views.GenreDelete.as_view(), name="genre-delete"),
    path('genre_edit/<int:pk>/', views.GenreEdit.as_view(), name="genre-edit"),
    path('publisher_list/', views.PublisherList.as_view(), name="publisher-list"),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name="publisher-view"),
    path('publisher_add/', views.PublisherAdd.as_view(), name="publisher-add"),
    path('publisher_delete/<int:pk>/', views.PublisherDelete.as_view(), name="publisher-delete"),
    path('publisher_edit/<int:pk>/', views.PublisherEdit.as_view(), name="publisher-edit"),
]