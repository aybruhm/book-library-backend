# Django Imports
from django.urls import path

# API View Imports
from books.views import (
    BooksAPIView, GetBookAPIView,
    AuthorAPIView
)


urlpatterns = [
    # books endpoint
    path("books/", BooksAPIView.as_view(), name="books"),
    path("book/<int:id>/", GetBookAPIView.as_view(), name="book"),
    
    # authors endpoint
    path("authors/", AuthorAPIView.as_view(), name="authors")
]
