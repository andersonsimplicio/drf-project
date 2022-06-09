from rest_framework import serializers
from app.watchlist.models import Movie


def validateName(value):
    if len(value) < 2:
        raise serializers.ValidationError('Name is too short')
    else:
        return value


class MovieSerializer(serializers.Serializer):
    id =  serializers.IntegerField(read_only=True)
    name =  serializers.CharField(validators=[validateName])
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
    
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError('Name is too short')
    #     else:
    #         return value
        
    #     if value == "":
    #         raise serializers.ValidationError('Name isn\'t empty!')
    #     else:
    #         return value
    
    def validate(self, data):
        if data['name'] == data['descriptions']:
            raise serializers.ValidationError('Name and Description shold be different!')
        else:
            return data
              
              
          
        
        
        
        

