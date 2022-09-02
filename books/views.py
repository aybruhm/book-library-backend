# Rest Framework Imports
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import views, status, permissions

# Own Imports
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer

# Third party Imports
from rest_api_payload import success_response, error_response

# DRF Yasg Imports
from drf_yasg.utils import swagger_auto_schema



class BooksAPIView(views.APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request:Request) -> Response:
        books = Book.objects.all()
        serializer = self.serializer_class(books, many=True)
        
        payload = success_response(
            status=True, message="Books retrieved!",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)


class GetUpdateBookAPIView(views.APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request:Request, id:int) -> Response:
        
        try:
            book = Book.objects.get(id=id)
        except (Book.DoesNotExist, Exception):
            payload = error_response(
                status=False, message="Book does not exist!"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(book)
        payload = success_response(
            status=True, message="Book retrieved!",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=serializer_class)
    def put(self, request:Request, id:int) -> Response:
        
        try:
            book = Book.objects.get(id=id)
        except (Book.DoesNotExist, Exception):
            payload = error_response(
                status=False, message="Book does not exist!"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(instance=book, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            payload = success_response(
                status=True, message="Book updated!",
                data=serializer.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        
        else:
            payload = error_response(status=False, message=serializer.errors)
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        

class AuthorAPIView(views.APIView):
    serializer_class = AuthorSerializer
    permission_classes = (permissions.AllowAny, )
    
    def get(self, request:Request) -> Response:
        authors = Author.objects.all()
        serializer = self.serializer_class(authors, many=True)
        
        payload = success_response(
            status=True, message="Authors retrieved!",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)
    

class GetUpdateAuthorAPIView(views.APIView):
    serializer_class = AuthorSerializer
    permission_classes = (permissions.AllowAny, )
    
    def get(self, reqeust:Request, id:int) -> Response:
        
        try:
            author = Author.objects.get(id=id)
        except (Author.DoesNotExist, Exception):
            payload = error_response(
                status=False, message="Author does not exist!"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(author)
        payload = success_response(
            status=True, message="Author retrieved!",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=serializer_class)
    def put(self, request:Request, id:int) -> Response:
        
        try:
            author = Author.objects.get(id=id)
        except (Author.DoesNotExist, Exception):
            payload = error_response(
                status=False, message="Author does not exist!"
            )
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(instance=author, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            payload = success_response(
                status=True, message="Author updated!",
                data=serializer.data
            )
            return Response(data=payload, status=status.HTTP_200_OK)
        
        else:
            payload = error_response(status=False, message=serializer.errors)
            return Response(data=payload, status=status.HTTP_404_NOT_FOUND)
        
    
    
class CreateAuthorAPIView(views.APIView):
    serializer_class = AuthorSerializer
    permission_classes = (permissions.AllowAny, )
    
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request:Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            payload = success_response(
                status=True, message="Author created successfully!",
                data=serializer.data
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        
        else:
            payload = error_response(status=False, message=serializer.errors)
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        
        
class CreateBookAPIView(views.APIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.AllowAny, )
    
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request:Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            payload = success_response(
                status=True, message="Book created successfully!",
                data=serializer.data
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        
        else:
            payload = error_response(status=False, message=serializer.errors)
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)