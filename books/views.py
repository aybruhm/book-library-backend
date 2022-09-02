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
        