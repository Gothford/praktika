from rest_framework import generics
from . import serializers
from .models import *


# Create your views here.
class NewsList(generics.ListAPIView):
    queryset = New.objects.all().order_by('-date')
    serializer_class = serializers.NewsSerializer
