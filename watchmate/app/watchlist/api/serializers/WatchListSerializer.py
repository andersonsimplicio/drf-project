from rest_framework import serializers
from app.watchlist.models import (
    WatchList,
    StreamPlatform
    )


 

class WatchListSerializer(serializers.ModelSerializer):
        
    class Meta:
        model= WatchList
        fields = "__all__"
        
    
class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    
    watchlist = WatchListSerializer(many=True,read_only=True)
    
    class Meta:
        model= StreamPlatform
        fields = "__all__"




# class StreamPlatformSerializer(serializers.ModelSerializer):
#     watchlist = WatchListSerializer(many=True,read_only=True)
#     # watchlist = serializers.StringRelatedField(many=True,)
#     # watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only=True)    
#     # watchlist = serializers.HyperlinkedRelatedField(
#     #     many=True,
#     #     read_only=True,
#     #     view_name='movie-detail'
#     #     )    
    
#     class Meta:
#         model= StreamPlatform
#         fields = "__all__"