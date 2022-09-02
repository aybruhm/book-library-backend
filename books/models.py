from django.db import models


class Author(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    
    class Meta:
        verbose_name_plural = "Authors"
        db_table = "authors"
        
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    name = models.TextField()
    isbn = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = "Books"
        db_table = "books"
        
    def __str__(self) -> str:
        return self.name