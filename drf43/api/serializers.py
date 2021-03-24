from rest_framework import serializers
from .models import Singer,Song


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Song
        fields=['id','url','title','singer','duration']

class SingerSerializer(serializers.HyperlinkedModelSerializer):
    sungby=SongSerializer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields=['id','url','name','gender','sungby']