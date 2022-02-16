from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from mainapp.models import Restapi

class RestapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restapi
        fields = ('id', 'kod')