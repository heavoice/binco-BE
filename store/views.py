from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Tshirt
from .models import Jeans
from .serializers import TshirtSerializer
from .serializers import JeansSerializer

@api_view(['GET'])
def tshirt_list(request):
    tshirts = Tshirt.objects.all()
    serializer = TshirtSerializer(tshirts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def jeans_list(request):
    jeans = Jeans.objects.all()
    serializer = JeansSerializer(jeans, many=True)
    return Response(serializer.data)