from rest_framework import serializers
from .models import *


class PeopleSerializer(serializers.ModelSerializer):


    class Meta:
        model= People
        fields= '__all__'


        def validate(self, data):


            if data['first_name']:
                for n in data['first_name']:
                    if n.isdigit():
                        raise serializers.ValidationError({'error': "name cannot be numeric"})


            if data['last_name']:
                for n in data['last_name']:
                    if n.isdigit():
                        raise serializers.ValidationError({'error': "name cannot be numeric"})
                        
            return data

class AdultSerializer(serializers.ModelSerializer):
    class Meta:
        model= Adult
        fields='__all__'

class ChildrenSerializer(serializers.ModelSerializer):
    adults=AdultSerializer()
    class Meta:
        model= Children
        fields='__all__'
