from rest_framework import serializers
from . models import employees

class employees_serializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        #fields = ('first_name', 'last_name')
        fields = '__all__'