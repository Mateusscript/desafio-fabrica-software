from django.shortcuts import render
from rest_framework import status, views
from rest_framework.response import Response
from books.serializers import BookSerializer
from .models import Book, BookData
import requests

class BookListAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={serializer.data["title"]}')
            data = response.json()
            
            for item in data['items']:
                bookData = BookData(
                    book=serializer.instance,
                    title=item['volumeInfo']['title'],
                    author=item['volumeInfo']['authors'][0],
                    publisher=item['volumeInfo']['publisher'] if 'publisher' in item['volumeInfo'] else '',
                    image_link=item['volumeInfo']['imageLinks']['thumbnail'] if 'publisher' in item['volumeInfo'] else '',
                    description=item['volumeInfo']['description'],
                    info_link=item['volumeInfo']['infoLink']
                )

                bookData.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

