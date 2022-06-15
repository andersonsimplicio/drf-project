from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
# from rest_framework import mixins

from app.watchlist.models import (
    WatchList,
    StreamPlatform,
    Review
    )
from app.watchlist.api.serializers.WatchListSerializer import (
    WatchListSerializer,
    StreamPlatformSerializer,
    ReviewSerializer
    )

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewDetail(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    






class StreamPlatformAV(APIView):
    
    def get(self,request):
        platform = StreamPlatform.objects.all()
        serialize = StreamPlatformSerializer(platform,many=True,context={'request':request})
        return Response(serialize.data)
    
    def post(self,request):
        serialize = StreamPlatformSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

class StreamPlatformDetailAV(APIView):
    
    def get(self,request,pk): 
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Erros':'Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        
        serialize = StreamPlatformSerializer(stream,context={'request': request})
        return Response(serialize.data)
    
    def put(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serialize = StreamPlatformSerializer(stream,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.erros,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)
            stream.delete()
        except StreamPlatform.DoesNotExist:
            return Response({'Erros':'Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
         
class WatchListAV(APIView):
    
    def get(self, request):
        watchlist = WatchList.objects.all()
        serialize = WatchListSerializer(watchlist,many=True)  
        return Response(serialize.data)

    def post(self,request):
        serialize = WatchListSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)

class WatchDetailAV(APIView):
    
    def get(self,request,pk): 
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Erros':'Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        
        serialize =WatchListSerializer(watchlist)
        return Response(serialize.data)
    
    
    def put(self, request, pk):
        watchlist = WatchList.objects.get(pk=pk)
        serialize = WatchListSerializer(watchlist,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.erros,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
            watchlist.delete()
        except watchlist.DoesNotExist:
            return Response({'Erros':'Não encontrado!'},status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        

watch_list = WatchListAV.as_view()
watch_detail = WatchDetailAV.as_view()
stream_platform_list = StreamPlatformAV.as_view()
stream_platform_detail = StreamPlatformDetailAV.as_view()
review_list = ReviewList.as_view()
review_detail = ReviewDetail.as_view()



# class ReviewDetail(mixins.RetrieveModelMixin,
#                    generics.GenericAPIView,
#                    ):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)