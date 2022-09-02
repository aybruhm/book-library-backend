# Django Imports
from django.urls import path

# API View Imports
from books.views import (
    BooksAPIView
)


urlpatterns = [
    path("books/", BooksAPIView.as_view(), name="books"),
]
