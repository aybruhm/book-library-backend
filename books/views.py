# Rest Framework Imports
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import views, status, permissions

# Own Imports
from books.models import Author, Book
from books.serializers import AuthorSerializer, BookSerializer

# Third party Imports
from rest_api_payload import success_response, error_response



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


class GetBookAPIView(views.APIView):
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