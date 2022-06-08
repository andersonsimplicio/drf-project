# # -*- coding: utf-8 -*-
# from django.shortcuts import render
# from app.watchlist.models import Movie
# from django.http import JsonResponse
# from django.views.decorators.clickjacking import xframe_options_exempt
# # Create your views here.

# def moive_list(request):
#     movies = Movie.objects.all()
#     data = {
#             'Filmes':list(movies.values())
#         }
#     return JsonResponse(data)

# def movie_detail(request,pk):
#     movies = Movie.objects.get(pk=pk)
#     data = {
#             'Filme':movies.name,
#             'Descrição': movies.descriptions    ,
#             'active':movies.active
#         }
#     return JsonResponse(data)
    