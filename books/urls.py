# Django Imports
from django.urls import path

# API View Imports
from books.views import (
    BooksAPIView, GetBookAPIView,
    AuthorAPIView, GetAuthorAPIView,
    CreateAuthorAPIView, CreateBookAPIView
)


urlpatterns = [
    # books endpoints
    path("books/", BooksAPIView.as_view(), name="books"),
    path("book/<int:id>/", GetBookAPIView.as_view(), name="book"),
    
    # authors endpoints
    path("authors/", AuthorAPIView.as_view(), name="authors"),
    path("author/<int:id>/", GetAuthorAPIView.as_view(), name="author"),
    
    # create new resource endpoints
    path("author/", CreateAuthorAPIView.as_view(), name="create_author"),
    path("book/", CreateBookAPIView.as_view(), name="create_book"),
]
