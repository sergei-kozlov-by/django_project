from datetime import datetime
from django.urls import reverse_lazy
from django.views import generic
from . import models, forms
from django.contrib.auth.mixins import PermissionRequiredMixin

class AuthorList(PermissionRequiredMixin, generic.ListView):
    template_name = "handbook/author_list.html"
    model = models.Author
    paginate_by = 20
    permission_required = ('hb:author-list')
    login_url = "user_app:login"

class AuthorDetail(generic.DetailView):
    template_name = "handbook/author_view.html"
    model = models.Author

class AuthorAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "handbook/author_add.html"
    model = models.Author
    form_class = forms.AuthorAddForm
    permission_required = ('hb:author-add')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:author-view", kwargs={'pk' : self.object.pk})

class AuthorDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "handbook/author_delete.html"
    model = models.Author
    success_url = reverse_lazy("hb:author-list")
    permission_required = ('hb:author-delete')
    login_url = "user_app:login"

class AuthorEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "handbook/author_edit.html"
    model = models.Author
    form_class = forms.AuthorAddForm
    permission_required = ('hb:author-edit')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:author-view", kwargs={'pk' : self.object.pk})

class SerieList(PermissionRequiredMixin, generic.ListView):
    template_name = "handbook/serie_list.html"
    model = models.Serie
    paginate_by = 20
    permission_required = ('hb:serie-list')
    login_url = "user_app:login"

class SerieDetail(generic.DetailView):
    template_name = "handbook/serie_view.html"
    model = models.Serie

class SerieAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "handbook/serie_add.html"
    model = models.Serie
    form_class = forms.SerieAddForm
    permission_required = ('hb:serie-add')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:serie-view", kwargs={'pk' : self.object.pk})

class SerieDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "handbook/serie_delete.html"
    model = models.Serie
    success_url = reverse_lazy("hb:serie-list")
    permission_required = ('hb:serie-delete')
    login_url = "user_app:login"
    
class SerieEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "handbook/serie_edit.html"
    model = models.Serie
    form_class = forms.SerieAddForm
    permission_required = ('hb:serie-edit')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:serie-view", kwargs={'pk' : self.object.pk})

class GenreList(PermissionRequiredMixin, generic.ListView):
    template_name = "handbook/genre_list.html"
    model = models.Genre
    paginate_by = 20
    permission_required = ('hb:genre-list')
    login_url = "user_app:login"

class GenreDetail(generic.DetailView):
    template_name = "handbook/genre_view.html"
    model = models.Genre

class GenreAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "handbook/genre_add.html"
    model = models.Genre
    form_class = forms.GenreAddForm
    permission_required = ('hb:genre-add')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:genre-view", kwargs={'pk' : self.object.pk})

class GenreDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "handbook/genre_delete.html"
    model = models.Genre
    success_url = reverse_lazy("hb:genre-list")
    permission_required = ('hb:genre-delete')
    login_url = "user_app:login"
    
class GenreEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "handbook/genre_edit.html"
    model = models.Genre
    form_class = forms.GenreAddForm
    permission_required = ('hb:genre-edit')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:genre-view", kwargs={'pk' : self.object.pk})

class PublisherList(PermissionRequiredMixin, generic.ListView):
    template_name = "handbook/publisher_list.html"
    model = models.Publisher
    paginate_by = 20
    permission_required = ('hb:publisher-list')
    login_url = "user_app:login"

class PublisherDetail(generic.DetailView):
    template_name = "handbook/publisher_view.html"
    model = models.Publisher

class PublisherAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "handbook/publisher_add.html"
    model = models.Publisher
    form_class = forms.PublisherAddForm
    permission_required = ('hb:publisher-add')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:publisher-view", kwargs={'pk' : self.object.pk})

class PublisherDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "handbook/publisher_delete.html"
    model = models.Publisher
    success_url = reverse_lazy("hb:publisher-list")
    permission_required = ('hb:publisher-delete')
    login_url = "user_app:login"
    
class PublisherEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "handbook/publisher_edit.html"
    model = models.Publisher
    form_class = forms.PublisherAddForm
    permission_required = ('hb:publisher-edit')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("hb:publisher-view", kwargs={'pk' : self.object.pk})
