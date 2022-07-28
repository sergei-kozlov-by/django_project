from datetime import datetime
from django.urls import reverse_lazy
from django.views import generic
from . import models, forms

class HomePage(generic.TemplateView):
    template_name = "handbook/home.html"

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['today'] = datetime.now().date
        context['book_list'] = models.Book.objects.all()[:10]
        return context

class AuthorList(generic.ListView):
    template_name = "handbook/author_list.html"
    model = models.Author

class AuthorDetail(generic.DetailView):
    template_name = "handbook/item_view.html"
    model = models.Author

class AuthorAdd(generic.CreateView):
    template_name = "handbook/item_add.html"
    model = models.Author
    form_class = forms.AuthorAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:author-view", kwargs={'pk' : self.object.pk})

class AuthorDelete(generic.DeleteView):
    template_name = "handbook/item_delete.html"
    model = models.Author
    success_url = reverse_lazy("hb:author-list")

class AuthorEdit(generic.UpdateView):
    template_name = "handbook/item_edit.html"
    model = models.Author
    form_class = forms.AuthorAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:author-view", kwargs={'pk' : self.object.pk})

class SerieList(generic.ListView):
    template_name = "handbook/serie_list.html"
    model = models.Serie

class SerieDetail(generic.DetailView):
    template_name = "handbook/item_view.html"
    model = models.Serie

class SerieAdd(generic.CreateView):
    template_name = "handbook/item_add.html"
    model = models.Serie
    form_class = forms.SerieAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:serie-view", kwargs={'pk' : self.object.pk})

class SerieDelete(generic.DeleteView):
    template_name = "handbook/item_delete.html"
    model = models.Serie
    success_url = reverse_lazy("hb:serie-list")

class SerieEdit(generic.UpdateView):
    template_name = "handbook/item_edit.html"
    model = models.Serie
    form_class = forms.SerieAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:serie-view", kwargs={'pk' : self.object.pk})

class GenreList(generic.ListView):
    template_name = "handbook/genre_list.html"
    model = models.Genre

class GenreDetail(generic.DetailView):
    template_name = "handbook/item_view.html"
    model = models.Genre

class GenreAdd(generic.CreateView):
    template_name = "handbook/item_add.html"
    model = models.Genre
    form_class = forms.GenreAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:genre-view", kwargs={'pk' : self.object.pk})

class GenreDelete(generic.DeleteView):
    template_name = "handbook/item_delete.html"
    model = models.Genre
    success_url = reverse_lazy("hb:genre-list")

class GenreEdit(generic.UpdateView):
    template_name = "handbook/item_edit.html"
    model = models.Genre
    form_class = forms.GenreAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:genre-view", kwargs={'pk' : self.object.pk})

class PublisherList(generic.ListView):
    template_name = "handbook/publisher_list.html"
    model = models.Publisher

class PublisherDetail(generic.DetailView):
    template_name = "handbook/item_view.html"
    model = models.Publisher

class PublisherAdd(generic.CreateView):
    template_name = "handbook/item_add.html"
    model = models.Publisher
    form_class = forms.PublisherAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:publisher-view", kwargs={'pk' : self.object.pk})

class PublisherDelete(generic.DeleteView):
    template_name = "handbook/item_delete.html"
    model = models.Publisher
    success_url = reverse_lazy("hb:publisher-list")

class PublisherEdit(generic.UpdateView):
    template_name = "handbook/item_edit.html"
    model = models.Publisher
    form_class = forms.PublisherAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:publisher-view", kwargs={'pk' : self.object.pk})

class BookList(generic.ListView):
    template_name = "handbook/book_list.html"
    model = models.Book

class BookDetail(generic.DetailView):
    template_name = "handbook/book_view.html"
    model = models.Book
    
class BookAdd(generic.CreateView):
    template_name = "handbook/item_add.html"
    model = models.Book
    form_class = forms.BookAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:book-view", kwargs={'pk' : self.object.pk})

class BookDelete(generic.DeleteView):
    template_name = "handbook/item_delete.html"
    model = models.Book
    success_url = reverse_lazy("hb:book-list")

class BookEdit(generic.UpdateView):
    template_name = "handbook/item_edit.html"
    model = models.Book
    form_class = forms.BookAddForm

    def get_success_url(self) -> str:
        return reverse_lazy("hb:book-view", kwargs={'pk' : self.object.pk})