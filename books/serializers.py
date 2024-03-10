
from rest_framework import serializers
from books.models import Book, BookData

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class BooksDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookData
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    data = BooksDataSerializer(source='bookdata_set', many=True, required=False)

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'data']
