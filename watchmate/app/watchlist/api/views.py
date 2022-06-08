from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from app.watchlist.models import Movie
from app.watchlist.api.serializers.MovieSerializer import MovieSerializer

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serialize = MovieSerializer(movies,many=True)  
        return Response(serialize.data)
    
    if request.method=='POST':
        serialize = MovieSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.erros,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def movie_detail(request,pk):
    if request.method == 'GET':
        try:
            movies = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'Erros':'Movies Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        
        serialize = MovieSerializer(movies)
        return Response(serialize.data)
        
    if request.method == 'PUT':
       movies = Movie.objects.get(pk=pk)
       serialize = MovieSerializer(movies,data=request.data)
       if serialize.is_valid():
           serialize.save()
           return Response(serialize.data)
       else:
           return Response(serialize.erros,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        try:
            movies = Movie.objects.get(pk=pk)
            movies.delete()
        except Movie.DoesNotExist:
            return Response({'Erros':'Movies Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
        