from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Author, Book
from .forms import AuthorForm, BookForm


class AuthorListView(ListView):
    queryset = Author.objects.all()
    template_name = 'author_list.html'
    context_object_name = 'authors'

class AuthorDetailView(DetailView):
    queryset = Author.objects.all()
    template_name = 'author_detail.html'
    context_object_name = 'author'

class AuthorCreateView(CreateView):
    form_class = AuthorForm
    template_name = 'author_create.html'
    success_url = reverse_lazy('author_list')

class AuthorUpdateView(UpdateView):
    queryset = Author.objects.all()
    form_class = AuthorForm
    template_name = 'author_update.html'
    success_url = reverse_lazy('author_list')

class AuthorDeleteView(DeleteView):
    queryset = Author.objects.all()
    template_name = 'author_delete.html'
    success_url = reverse_lazy('author_list')





class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    queryset = Book.objects.all()
    template_name = 'book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    form_class = BookForm
    template_name = 'book_create.html'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    queryset = Book.objects.all()
    form_class = BookForm
    template_name = 'book_update.html'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    queryset = Book.objects.all()
    template_name = 'book_delete.html'
    success_url = reverse_lazy('book_list')