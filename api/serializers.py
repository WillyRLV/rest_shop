from rest_framework import serializers


from .models import (Material, Funcion)

class MaterialSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Material
        fields = '__all__'

class FuncionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Funcion
        fields = '__all__'

