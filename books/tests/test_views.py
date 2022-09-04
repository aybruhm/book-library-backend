# Native Imports
import json

# Third Party Imports
from rest_api_payload import success_response, error_response

# Django Imports
from django.urls import reverse

# Rest Framework Imports
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

# Own Imports
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer


# Initialize api client
client = APIClient()


class BooksTestCase(APITestCase):
    """Test case to get all the books api"""
    
    def setUp(self) -> None:
        Book.objects.create(name="Glitch", isbn="1256841190", author=Author.objects.get_or_create(id=1)[0])
        Book.objects.create(name="Software Architectural Patterns", isbn="3433549941", author=Author.objects.get_or_create(id=3)[0])
        Book.objects.create(name="Clean Code", isbn="0875754570", author=Author.objects.get_or_create(id=2)[0])
    
    def test_get_all_books(self):
        """
        Test that the response data from the API is equal 
        to the serialized data of all the books in the database
        
        :return: A response object data and status_code 200
        """
        response = client.get(reverse("books"))
    
        books = Book.objects.all()
        
        serializer = BookSerializer(books, many=True)
        serializer_data = success_response(status=True, message="Books retrieved!", data=serializer.data)
        
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        
class BookTestCase(APITestCase):
    """Test case to create and get a single book api"""
    
    def setUp(self) -> None:
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.book = Book.objects.create(name="Return of Glitch X", isbn="1256841190", author=self.author)
        self.valid_payload = {
            "name": "Pythonic Code",
            "isbn": "2738294838",
            "author": {
                "first_name": self.author.first_name,
                "last_name": self.author.last_name
            }
        }
        self.invalid_payload = {
            "name": "",
            "isbn": "0875754570",
            "author": {
                "first_name": "Doe",
                "last_name": ""
            }
        }
    
    def test_get_single_book(self):
        """
        Test that the response data from the API is equal 
        to the serialized data of the book object
        
        :return: A response object data and status_code 200
        """
        response = client.get(reverse('book', args=[self.book.id]))        
        book = Book.objects.get(id=self.book.id)
        
        serializer = BookSerializer(book)
        serializer_data = success_response(status=True, message="Book retrieved!", data=serializer.data)
        
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_valid_book(self):
        """
        Test case to send a POST request to the create_book 
        endpoint with a valid payload
        
        :return: A response status_code 201
        """
        response = client.post(
            reverse('create_book'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_create_invalid_book(self):
        """
        Test case to send a POST request to the create_book 
        endpoint with an invalid payload
        
        :return: A response status_code 400
        """
        response = client.post(
            reverse('create_book'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

class UpdateSingleBookTestCase(APITestCase):
    """Test case to update a single book api"""
    
    def setUp(self) -> None:
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.book = Book.objects.create(name="Return of Glitch X", isbn="1256841190", author=self.author)
        self.valid_payload = {
            "name": "Glitch",
            "isbn": "2738534838",
            "author": {
                "first_name": "Victor",
                "last_name": "Martin"
            }
        }
        self.invalid_payload = {
            "name": "",
            "isbn": "2738534838",
            "author": {
                "first_name": "Victor",
                "last_name": 456
            }
        }
    
    def test_valid_update_single_book(self):
        """
        Test case to send a PUT request to the book endpoint with the book id, 
        and the valid payload
        
        :return: A response status_code 200
        """
        response = client.put(
            reverse('book', args=[self.book.id]),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_invalid_update_single_book(self):
        """
        Test case to update a book with invalid data
        
        :return: A response status_code 400
        """
        response = client.put(
            reverse('book', args=[self.book.id]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
    def test_update_single_book_not_found(self):
        """
        Test case to update a book that doesn't exist
        
        :return: A response status_code 404
        """
        response = client.put(
            reverse('book', args=[53]),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)    
    

class AuthorsTestCase(APITestCase):
    """Test case to get all the authors api"""
    
    def setUp(self) -> None:
        Author.objects.create(first_name="Jane", last_name="Doe")
        Author.objects.create(first_name="Flutter", last_name="Wave")
        Author.objects.create(first_name="Waje", last_name="Solutions")
    
    def test_get_all_authors(self):
        """
        Test that the response data from the API is equal
        to the serialized data of all the authors in the database
        
        :return: A response object data and status_code 200
        """
        response = client.get(reverse("authors"))
    
        authors = Author.objects.all()
        
        serializer = AuthorSerializer(authors, many=True)
        serializer_data = success_response(status=True, message="Authors retrieved!", data=serializer.data)
        
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    

class AuthorTestCase(APITestCase):
    """Test case to create and get a single author api"""
    
    def setUp(self) -> None:
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.valid_payload = {
            "first_name": "Clever",
            "last_name": "Programmer"
        }
        self.invalid_payload = {
            "first_name": "",
            "last_name": 37384947584
        }
    
    def test_get_single_author(self):
        """
        Test that the response data from the API is equal 
        to the serialized data of the author object
        
        :return: A response object data and status_code 200
        """
        response = client.get(reverse('author', args=[self.author.id]))        
        author = Author.objects.get(id=self.author.id)
        
        serializer = AuthorSerializer(author)
        serializer_data = success_response(status=True, message="Author retrieved!", data=serializer.data)
        
        self.assertEqual(response.data, serializer_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_valid_author(self):
        """
        Test case to send a POST request to the create_author 
        endpoint with a valid payload
        
        :return: A response status_code 201
        """
        response = client.post(
            reverse('create_author'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_create_invalid_author(self):
        """
        Test case to send a POST request to the create_author 
        endpoint with an invalid payload
        
        :return: A response status_code 400
        """
        response = client.post(
            reverse('create_author'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  

class UpdateSingleAuthorTestCase(APITestCase):
    """Test case to update a single author api"""
    
    def setUp(self) -> None:
        self.author = Author.objects.create(first_name="John", last_name="Doe")
        self.valid_payload = {
            "first_name": "Qazi",
            "last_name": self.author.last_name
        }
        self.invalid_payload = {
            "first_name": "",
            "last_name": 37384947584
        }
    
    def test_valid_update_single_author(self):
        """
        Test case to send a PUT request to the author endpoint with the author id, 
        and the valid payload
        
        :return: A response status_code 200
        """
        response = client.put(
            reverse('author', args=[self.author.id]),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_invalid_update_single_author(self):
        """
        Test case to update an author with invalid data
        
        :return: A response status_code 400
        """
        response = client.put(
            reverse('author', args=[self.author.id]),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_update_single_author_not_found(self):
        """
        Test case to update an author that doesn't exist
        
        :return: A response status_code 404
        """
        response = client.put(
            reverse('author', args=[53]),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )        
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    