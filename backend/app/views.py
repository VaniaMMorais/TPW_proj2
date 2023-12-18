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
    if request.method == 'POST':
        serializer = IngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_ingredient(request, ing_id):
    ingrediente = get_object_or_404(Ingrediente, id=ing_id)

    if request.method == 'PUT':
        serializer = IngredienteSerializer(ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_ingredient(request, ing_id):
    ingrediente = get_object_or_404(Ingrediente, id=ing_id)

    if request.method == 'DELETE':
        ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def ingredient_detail(request, ing_id):
    ingrediente = get_object_or_404(Ingrediente, id=ing_id)

    if request.method == 'GET':
        serializer = IngredienteSerializer(ingrediente)
        return Response(serializer.data)