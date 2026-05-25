from rest_framework import serializers
from .models import Tshirt
from .models import Jeans

class TshirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tshirt
        fields = '__all__'

class JeansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jeans
        fields = '__all__'