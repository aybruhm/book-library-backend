# Rest Framework Imports
from rest_framework import serializers

# Own Imports
from books.models import Author, Book



class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name")
        
        

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = ("id", "name", "isbn", "author")