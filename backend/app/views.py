from datetime import datetime,date

from rest_framework import status
from rest_framework.parsers import JSONParser,MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *
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


#utilizadores
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import urlsafe_base64_decode
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .tokens import generate_token
from .forms import UserProfileForm

from .serializers import UserSerializer



#################################################### INGREDIENTES ####################################################

@api_view(['GET', 'POST'])
def categoria_ingredientes(request):
    if request.method == 'GET':
        categoria_ingredientes = CategoriaIngrediente.objects.all()
        serializer = CategoriaIngredienteSerializer(categoria_ingredientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaIngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def categoria_ingrediente_detail(request, pk):
    try:
        categoria_ingrediente = CategoriaIngrediente.objects.get(pk=pk)
    except CategoriaIngrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaIngredienteSerializer(categoria_ingrediente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaIngredienteSerializer(categoria_ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria_ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_ingredient(request):
    serializer = IngredienteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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

#################################################### RECEITAS ####################################################

@api_view(['GET', 'POST'])
def categorias(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def categoria_detail(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CategoriaSerializer(categoria, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        categoria.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def create_receita(request):
    serializer = ReceitaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def receitas(request):
    receitas = Receita.objects.all()
    serializer = ReceitaSerializer(receitas, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def receita_detail(request, id):
    try:
        receita = Receita.objects.get(pk=id)
    except Receita.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ReceitaSerializer(receita)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReceitaSerializer(receita, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        receita.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################## ASSOCIAÇÃO: RECEITA/INGREDIENTE ##############################################

@api_view(['GET', 'POST'])
def receita_ingredientes(request):
    if request.method == 'GET':
        receita_ingredientes = ReceitaIngrediente.objects.all()
        serializer = ReceitaIngredienteSerializer(receita_ingredientes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReceitaIngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def receita_ingrediente_detail(request, pk):
    receita_ingrediente = get_object_or_404(ReceitaIngrediente, pk=pk)

    if request.method == 'GET':
        serializer = ReceitaIngredienteSerializer(receita_ingrediente)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReceitaIngredienteSerializer(receita_ingrediente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        receita_ingrediente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################## AVALIAÇÕES ##############################################
    
@api_view(['GET', 'POST'])
def avaliacoes(request):
    if request.method == 'GET':
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def avaliacao_detail(request, pk):
    try:
        avaliacao = Avaliacao.objects.get(pk=pk)
    except Avaliacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AvaliacaoSerializer(avaliacao)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AvaliacaoSerializer(avaliacao, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        avaliacao.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


################################## FRIGORÍFICO ##############################################
    
@api_view(['GET', 'POST'])
def frigorificos(request):
    if request.method == 'GET':
        frigorificos = Frigorifico.objects.all()
        serializer = FrigorificoSerializer(frigorificos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FrigorificoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def frigorifico_detail(request, pk):
    try:
        frigorifico = Frigorifico.objects.get(pk=pk)
    except Frigorifico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FrigorificoSerializer(frigorifico)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FrigorificoSerializer(frigorifico, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        frigorifico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

################################## FAVORITOS ##############################################
    
@api_view(['GET', 'POST'])
def favoritos(request):
    if request.method == 'GET':
        favoritos = Favoritos.objects.all()
        serializer = FavoritosSerializer(favoritos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FavoritosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def favoritos_detail(request, pk):
    try:
        favoritos = Favoritos.objects.get(pk=pk)
    except Favoritos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FavoritosSerializer(favoritos)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FavoritosSerializer(favoritos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        favoritos.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

################################## LISTA DE COMPRAS ##############################################
    
@api_view(['GET', 'POST'])
def listas_compras(request):
    if request.method == 'GET':
        listas_compras = ListaCompras.objects.all()
        serializer = ListaComprasSerializer(listas_compras, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ListaComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lista_compras_detail(request, pk):
    try:
        lista_compras = ListaCompras.objects.get(pk=pk)
    except ListaCompras.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ListaComprasSerializer(lista_compras)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ListaComprasSerializer(lista_compras, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lista_compras.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################################################### UTILIZADORES ####################################################
class ProfileView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)