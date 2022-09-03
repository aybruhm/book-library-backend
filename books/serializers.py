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
    author = AuthorSerializer()
    
    class Meta:
        model = Book
        fields = ("id", "name", "isbn", "author")
    
    def create(self, validated_data:dict):
        
        # get fields from validated data
        _author = validated_data.get("author")
        name = validated_data.get("name")
        isbn = validated_data.get("isbn")
        
        # gets or creates and save author object to database
        try:
            author = Author.objects.get(
                first_name=_author.get("first_name"), 
                last_name=_author.get("last_name")
            )
        except (Author.DoesNotExist, Exception):
            author = Author.objects.create(
                first_name=str(_author.get("first_name")).capitalize, 
                last_name=str(_author.get("last_name")).capitalize
            ).save()
        
        # creates and save book object to database
        book = Book.objects.create(name=name, isbn=isbn, author=author)
        book.save()
        return book
    
    def update(self, instance, validated_data):
        # get author data
        author_data = validated_data.pop("author")
        
        # get fields from validated data
        name = validated_data.get("name")
        isbn = validated_data.get("isbn")
        
        # get or create author object to database
        author, _ = Author.objects.get_or_create(**author_data)
        
        # update book object to database
        instance.author = author
        instance.name = name
        instance.isbn = isbn
        instance.save()
        return instance