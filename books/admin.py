# Django Imports
from django.contrib import admin

# Own Imports
from books.models import Book, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "isbn", "author"]
    

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name"]