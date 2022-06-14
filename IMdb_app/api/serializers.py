from dataclasses import fields
from pyexpat import model
from unicodedata import name
from rest_framework import serializers
from IMdb_app.models import watchlist, StreamPlatform, Review

class Reviewserializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = '__all__'


class watchlistSerializer(serializers.ModelSerializer):
    # reviews = Reviewserializer(many= True, read_only = True)
    platform = serializers.CharField(source= 'platform.name')

    class Meta:
        model = watchlist
        fields = '__all__'


class StreamingSerializer(serializers.ModelSerializer):
    watchlists = watchlistSerializer(many= True, read_only = True)

    #to show only name 
    # watchlists = serializers.StringRelatedField(many= True, read_only = True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'

        
    


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate_name(self, value):
#         if len(value)<2:
#             raise serializers.ValidationError("movie title too short..!!!")    
#         else:
#             return value
    

#     def validate_Object(self,data):
#         if data['name']== data['description']:
#             raise serializers.ValidationError("title & description should be different")
#         else:
#             return data
              

