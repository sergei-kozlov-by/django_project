from django.shortcuts import render
from django.views import generic
from . import models, forms

# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "handbook/home.html"

class AuthorList(generic.ListView):
    template_name = "handbook/author_list.html"
    model = models.Author

class AuthorDetail(generic.DetailView):
    template_name = "handbook/author_view.html"
    model = models.Author

class AuthorAdd(generic.CreateView):
    template_name = "handbook/author_add.html"
    model = models.Author
    form_class = forms.AuthorAddForm

    def get_success_url(self):
        return f"/author/{self.object.pk}/"

class AuthorDelete(generic.DeleteView):
    template_name = "handbook/author_delete.html"
    model = models.Author
    success_url = "/author_list/"

class AuthorEdit(generic.UpdateView):
    template_name = "handbook/author_edit.html"
    model = models.Author
    form_class = forms.AuthorAddForm

    def get_success_url(self):
        return f"/author/{self.object.pk}/"

class SerieList(generic.ListView):
    template_name = "handbook/serie_list.html"
    model = models.Serie

class SerieDetail(generic.DetailView):
    template_name = "handbook/serie_view.html"
    model = models.Serie

class SerieAdd(generic.CreateView):
    template_name = "handbook/serie_add.html"
    model = models.Serie
    form_class = forms.SerieAddForm

    def get_success_url(self):
        return f"/serie/{self.object.pk}/"

class SerieDelete(generic.DeleteView):
    template_name = "handbook/serie_delete.html"
    model = models.Serie
    success_url = "/serie_list/"

class SerieEdit(generic.UpdateView):
    template_name = "handbook/serie_edit.html"
    model = models.Serie
    form_class = forms.SerieAddForm

    def get_success_url(self):
        return f"/serie/{self.object.pk}/"

class GenreList(generic.ListView):
    template_name = "handbook/genre_list.html"
    model = models.Genre

class GenreDetail(generic.DetailView):
    template_name = "handbook/genre_view.html"
    model = models.Genre

class GenreAdd(generic.CreateView):
    template_name = "handbook/genre_add.html"
    model = models.Genre
    form_class = forms.GenreAddForm

    def get_success_url(self):
        return f"/genre/{self.object.pk}/"

class GenreDelete(generic.DeleteView):
    template_name = "handbook/genre_delete.html"
    model = models.Genre
    success_url = "/genre_list/"

class GenreEdit(generic.UpdateView):
    template_name = "handbook/genre_edit.html"
    model = models.Genre
    form_class = forms.GenreAddForm

    def get_success_url(self):
        return f"/genre/{self.object.pk}/"

class PublisherList(generic.ListView):
    template_name = "handbook/publisher_list.html"
    model = models.Publisher

class PublisherDetail(generic.DetailView):
    template_name = "handbook/publisher_view.html"
    model = models.Publisher

class PublisherAdd(generic.CreateView):
    template_name = "handbook/publisher_add.html"
    model = models.Publisher
    form_class = forms.PublisherAddForm

    def get_success_url(self):
        return f"/publisher/{self.object.pk}/"

class PublisherDelete(generic.DeleteView):
    template_name = "handbook/publisher_delete.html"
    model = models.Publisher
    success_url = "/publisher_list/"

class PublisherEdit(generic.UpdateView):
    template_name = "handbook/publisher_edit.html"
    model = models.Publisher
    form_class = forms.PublisherAddForm

    def get_success_url(self):
        return f"/publisher/{self.object.pk}/"

class BookList(generic.ListView):
    template_name = "handbook/book_list.html"
    model = models.Book

class BookDetail(generic.DetailView):
    template_name = "handbook/book_view.html"
    model = models.Book

class BookAdd(generic.CreateView):
    template_name = "handbook/book_add.html"
    model = models.Book
    form_class = forms.BookAddForm

    def get_success_url(self):
        return f"/book/{self.object.pk}/"

class BookDelete(generic.DeleteView):
    template_name = "handbook/book_delete.html"
    model = models.Book
    success_url = "/book_list/"

class BookEdit(generic.UpdateView):
    template_name = "handbook/book_edit.html"
    model = models.Book
    form_class = forms.BookAddForm

    def get_success_url(self):
        return f"/book/{self.object.pk}/"
        