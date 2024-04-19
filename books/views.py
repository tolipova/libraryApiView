from django.shortcuts import render, HttpResponse
from django.http import Http404
from .models import *
from .serializers import *
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
# Create your views here.
class BookListApiView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializers_data = BookSerializers(books, many=True).data
        
        data = {
            "status" : f"Returned {len(books)} books",
            "books" : serializers_data
        }
        return Response(data)
    
class BooksCreateApiView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status":"Books are saved to the database",
                "books":data
            }
            return Response(data)
        else:
            return Response(
                {"status":False,
                 "message":"Seriliazer is not valid"}, status=status.HTTP_400_BAD_REQUEST
            )
                
# class BookListApiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

class BookDetailApiView(APIView):
    def get(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            serializer_data = BookSerializers(book).data
            
            data = {
                "status":"Successfull",
                "book":serializer_data
            } 
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response(
                {
                    "status":"Does not exits",
                    "message":"Book is not found"
                }, status=status.HTTP_404_NOT_FOUND
            )      
         
# class BookDetailApiView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

# class BookDeleteApiView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
class BookDeleteApiView(APIView):
      def delete(self, request, pk):
          try:
            book = Book.objects.get_object_or_404(id=pk)
            book.delete()
            return Response(
                {"status":True,
                "message":"Successfully deleted!"}
            )
          except Exception:
              return Response(
                  {"status":False,
                   "message":"Book is not found"}
              )
              
# class BookUpdateApiView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
class BookUpdateApiView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serializer = BookSerializers(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
            return Response({
                "status":True,
                "message":f"Book {book_saved} updated successfully!"
            })
        else:
            return Response(
                {
                    "status":False,
                    "message":"Book is not found"
                }
            )
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
