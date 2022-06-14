# from django.shortcuts import render
# from .models import Movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()    #retreiving data (complex datatype)
#     data = { 'movies': list(movies.values())}    #serializing manually   (python data type)
#     return JsonResponse(data)

# def movie_detail(request,pk):
#     movie_detail = Movie.objects.get(pk=pk)      #retreiving data (complex datatype)
#     data = { 'name': movie_detail.name, 'desc': movie_detail.description, 'active': movie_detail.active }      #serializing manually  (python data type)
#     return JsonResponse(data)


