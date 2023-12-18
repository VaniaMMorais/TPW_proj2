from datetime import datetime,date

from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import Ingrediente
from .serializers import IngredienteSerializer
from .forms import *

from django.core.files.base import ContentFile

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse, JsonResponse 

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils import timezone

from . tokens import generate_token
from webproj import settings

from django.core.mail import EmailMessage, send_mail

from django.template.loader import render_to_string

from django.db.models import Avg
from django.db.models import Count

from unidecode import unidecode
import re
import base64


#################################################### INGREDIENTES ####################################################

@api_view(['POST'])
def create_ingredient(request):
    serializer = IngredienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def ingredientes(request):
    ingrediente = Ingrediente.objects.all()
    serializer = IngredienteSerializer(ingrediente, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def ingredient_detail(request, id):

    try:
        ingredient = Ingrediente.objects.get(pk=id)
    except Ingrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = IngredienteSerializer(ingredient)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = IngredienteSerializer(ingredient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
        ingredient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


