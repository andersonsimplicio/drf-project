from rest_framework import serializers
from app.watchlist.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    len_name =  serializers.SerializerMethodField()
    
    class Meta:
        model= Movie
        fields = "__all__"
    
    def get_len_name(self, object):
        return len(object.name)
       
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')
        else:
            return value
        
        if value == "":
            raise serializers.ValidationError('Name isn\'t empty!')
        else:
            return value
    
    def validate(self, data):
        if data['name'] == data['descriptions']:
            raise serializers.ValidationError('Name and Description shold be different!')
        else:
            return data
    