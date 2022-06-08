from rest_framework import serializers
from app.watchlist.models import Movie

class MovieSerializer(serializers.Serializer):
    id =  serializers.IntegerField(read_only=True)
    name =  serializers.CharField()
    descriptions =  serializers.CharField()
    active =  serializers.BooleanField()
    
    def create(self,validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self,instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.descriptions = validated_data.get('descriptions',instance.descriptions)
        instance.active = validated_data.get('active',instance.active)
        instance.save()
        return instance
        
        
        

