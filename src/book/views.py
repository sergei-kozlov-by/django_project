from datetime import datetime
from django.urls import reverse_lazy
from django.views import generic
from . import models, forms
from django.contrib.auth.mixins import PermissionRequiredMixin

class HomePage(generic.TemplateView):
    template_name = "book/home.html"

    def get_context_data(self, *args, **kwargs):
        context =  super().get_context_data(*args, **kwargs)
        context['book_list'] = models.Book.objects.all()[:10]
        return context

class BookList(generic.ListView):
    template_name = "book/book_list.html"
    model = models.Book
    paginate_by = 20

class BookDetail(generic.DetailView):
    template_name = "book/book_view.html"
    model = models.Book
    
class BookAdd(PermissionRequiredMixin, generic.CreateView):
    template_name = "book/book_add.html"
    model = models.Book
    form_class = forms.BookAddForm
    permission_required = ('book:book-add')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("book:book-view", kwargs={'pk' : self.object.pk})

class BookDelete(PermissionRequiredMixin, generic.DeleteView):
    template_name = "book/book_delete.html"
    model = models.Book
    success_url = reverse_lazy("book:book-list")
    permission_required = ('book:book-delete')
    login_url = "user_app:login"

class BookEdit(PermissionRequiredMixin, generic.UpdateView):
    template_name = "book/book_edit.html"
    model = models.Book
    form_class = forms.BookAddForm
    permission_required = ('book:book-edit')
    login_url = "user_app:login"

    def get_success_url(self) -> str:
        return reverse_lazy("book:book-view", kwargs={'pk' : self.object.pk})
