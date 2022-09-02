# Rest Framework Imports
from rest_framework import serializers

# Own Imports
from books.models import Author, Book



class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ("id", "first_name", "last_name")      
        
    def create(self, validated_data:dict):
        author = Author.objects.create(**validated_data)
        author.save()
        return author
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    
    class Meta:
        model = Book
        fields = ("id", "name", "isbn", "author")
    