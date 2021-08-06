from .models import Person, Group
from rest_framework import serializers


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = '__all__'
