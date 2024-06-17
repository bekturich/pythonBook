from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
urlpatterns = [
    path('', AuthorListView.as_view(), name='author_list'),
    path('<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('create/', AuthorCreateView.as_view(), name='author_create'),
    path('<int:pk>/update/', AuthorUpdateView.as_view(), name='author_update'),
    path('<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),

    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]