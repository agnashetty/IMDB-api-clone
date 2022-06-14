import re
from urllib import request
from wsgiref import validate
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics, viewsets
from rest_framework.exceptions import ValidationError
from django.core import validators
from rest_framework.permissions import IsAuthenticated


from IMdb_app.models import watchlist, StreamPlatform, Review
from .serializers import Reviewserializer, watchlistSerializer, StreamingSerializer
from .permissions import AdminorReadonly, object_permission

# <-------------MODEL VIEWSET--------------->
# class StreamingPlatform(viewsets.ModelViewSet):
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamingSerializer




# <-------------VIEWSET--------------->
# class StreamingPlatform(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving movielist.
#     """
#     def list(self, request):
#         queryset =StreamPlatform.objects.all()
#         serializer = StreamingSerializer(queryset, many=True)
#         return Response(serializer.data)
     

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = status.get_object_or_404(queryset, pk=pk)
#         serializer = StreamingSerializer(watchlist)
#         return Response(serializer.data)




# <-----------GENERIC CONCRETE VIEW--------------->
class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = Reviewserializer
   
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)





class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = Reviewserializer
    permission_classes = [object_permission]



class AddReview(generics.CreateAPIView):
    serializer_class = Reviewserializer
    permission_classes = [IsAuthenticated]
    


    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):

        pk = self.kwargs.get('pk')
        movie = watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist = movie, user = review_user)
        
        if review_queryset.exists():
            raise ValidationError("You have already reviewed this watchlist")

        # if watchlist.no_of_rating == 0:
        #     serializer.is_valid()
        #     watchlist.avg_rate = serializer.validated_data.get('rating')

        # else:
        #     watchlist.avg_rate = (watchlist.avg_rate + serializer.validated_data.get('rating'))/2
           
        # watchlist.no_of_rating = watchlist.no_of_rating + 1
        # watchlist.save()
 
        serializer.save(watchlist = movie, user = review_user)



# <-----------GENERIC VIEW--------------->
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = Reviewserializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = Reviewserializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)




#  <---------- CLASS BASED VIEW-------->
class watchlistAV(APIView):
    permission_classes = [AdminorReadonly]
    def get(self, request):
        watchlists = watchlist.objects.all()
        serializer = watchlistSerializer(watchlists, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = watchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class watchlistDetailAV(APIView):
    permission_classes = [AdminorReadonly]
    def get(self,request,pk):
        try:
            movie_detail = watchlist.objects.get(pk=pk)
        except:
            return Response({'error: movie not found'}, status= status.HTTP_400_BAD_REQUEST)
        serializer = watchlistSerializer(movie_detail)
        return Response(serializer.data)
    
    def put(self,request,pk):
        movie_detail = watchlist.objects.get(pk=pk)
        serializer = watchlistSerializer(movie_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        movie_detail = watchlist.objects.get(pk=pk)
        movie_detail.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



class StreamingPlatform(APIView):
    permission_classes = [AdminorReadonly]
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamingSerializer(platforms, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = StreamingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatform_Detail(APIView):
    permission_classes = [AdminorReadonly]
    def get(self,request,pk):
        try:
            platform_detail = StreamPlatform.objects.get(pk=pk)
        except:
            return Response({'error: streaming platform doesn\'t exist'}, status= status.HTTP_400_BAD_REQUEST)
        serializer = StreamingSerializer(platform_detail)
        return Response(serializer.data)
    
    def put(self,request,pk):
        platform_detail = StreamPlatform.objects.get(pk=pk)
        serializer = StreamingSerializer(platform_detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        platform_detail = StreamPlatform.objects.get(pk=pk)
        platform_detail.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)



  # <---------- FUNCTION BASED VIEW-------->
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save() 
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request,pk):
#     if request.method == 'GET':
#         try:
#             movie_detail = Movie.objects.get(pk=pk)
#         except:
#             return Response({'error: movie not found'}, status= status.HTTP_400_BAD_REQUEST)
#         serializer = MovieSerializer(movie_detail)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         movie_detail = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie_detail, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     if request.method == 'DELETE':
#         movie_detail = Movie.objects.get(pk=pk)
#         movie_detail.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)      




    