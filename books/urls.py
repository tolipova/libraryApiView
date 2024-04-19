from django.urls import path
from .views import *
urlpatterns = [
    path('books', BookListApiView.as_view(), ),
    path('books-create', BooksCreateApiView.as_view()),
    path('book/', BookListCreateView.as_view()),
    path('<int:pk>/updel/', BookUpdateDeleteView.as_view()),
    path('<int:pk>/', BookDetailApiView.as_view(), ),
    path('<int:pk>/update/', BookUpdateApiView.as_view(), ),
    path('<int:pk>/delete/', BookDeleteApiView.as_view(), )
]
