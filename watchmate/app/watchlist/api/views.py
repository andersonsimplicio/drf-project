from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from app.watchlist.models import Movie
from app.watchlist.api.serializers.MovieSerializer import MovieSerializer



class MovieListAV(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serialize = MovieSerializer(movies,many=True)  
        return Response(serialize.data)

    def post(self,request):
        serialize = MovieSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAV(APIView):
    
    def get(self,request,pk): 
        try:
            movies = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Erros':'Movies Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        
        serialize = MovieSerializer(movies)
        return Response(serialize.data)
    def put(self,request,pk):
        movies = Movie.objects.get(pk=pk)
        serialize = MovieSerializer(movies,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.erros,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            movies = Movie.objects.get(pk=pk)
            movies.delete()
        except Movie.DoesNotExist:
            return Response({'Erros':'Movies Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

movie_list = MovieListAV.as_view()
movie_detail = MovieDetailAV.as_view()

