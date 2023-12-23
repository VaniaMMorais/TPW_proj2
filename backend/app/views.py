from datetime import datetime,date

from rest_framework import status
from rest_framework.parsers import JSONParser,MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication

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

# filtrar receitas
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics
from django.db.models import Avg
from django.db.models import Q
from django.http import JsonResponse


#################################################### INGREDIENTES ####################################################

@api_view(['GET'])
def all_categoria_ingredientes(request):
    if request.method == 'GET':
        categoria_ingredientes = CategoriaIngrediente.objects.all()
        serializer = CategoriaIngredienteSerializer(categoria_ingredientes, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_categoria_ingrediente(request):
        serializer = CategoriaIngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def categoria_ingrediente_detail(request, pk):
    try:
        categoria_ingrediente = CategoriaIngrediente.objects.get(pk=pk)
    except CategoriaIngrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriaIngredienteSerializer(categoria_ingrediente)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_categoria_ingrediente(request, pk):
    try:
        categoria_ingrediente = CategoriaIngrediente.objects.get(pk=pk)
    except CategoriaIngrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriaIngredienteSerializer(categoria_ingrediente, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_categoria_ingrediente(request, pk):
    try:
        categoria_ingrediente = CategoriaIngrediente.objects.get(pk=pk)
    except CategoriaIngrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

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

@api_view(['GET'])
def get_ingredient_detail(request, id):
    try:
        ingredient = Ingrediente.objects.get(pk=id)
    except Ingrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = IngredienteSerializer(ingredient)
    return Response(serializer.data)

@api_view(['PUT'])
def update_ingredient(request, id):
    try:
        ingredient = Ingrediente.objects.get(pk=id)
    except Ingrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = IngredienteSerializer(ingredient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_ingredient(request, id):
    try:
        ingredient = Ingrediente.objects.get(pk=id)
    except Ingrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    ingredient.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

#################################################### RECEITAS ####################################################

@api_view(['GET'])
def categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_categoria(request):
    
    serializer = CategoriaSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def categoria_detail(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriaSerializer(categoria)
    return Response(serializer.data)

@api_view(['PUT'])
def edit_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_categoria(request, pk):
    try:
        categoria = Categoria.objects.get(pk=pk)
    except Categoria.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    categoria.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

    
@api_view(['POST'])
def create_receita(request):
    # Parse o JSON manualmente para obter a categoria
    data = JSONParser().parse(request)
    categoria_id = data.get('category')

    # Verifica se a categoria existe
    try:
        categoria = Categoria.objects.get(pk=categoria_id)
    except Categoria.DoesNotExist:
        return Response({'category': ['Categoria não encontrada.']}, status=status.HTTP_400_BAD_REQUEST)

    # Adiciona a categoria ao dicionário de dados
    data['category'] = categoria_id

    # Cria o serializer com os dados ajustados
    serializer = ReceitaSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def receitas(request):
    receitas = Receita.objects.all()
    receitas_data = []

    for receita in receitas:
        receita_data = {
            'user': receita.user.username if receita.user else '',
            'category': receita.category.name if receita.category else '',
            'name': receita.name,
            'description': receita.description,
            'tempoPreparacao': receita.tempoPreparacao,
            'tempoCozinhar': receita.tempoCozinhar,
            'quantidadePessoas': receita.quantidadePessoas,
            'nivel': receita.nivel,
            'imagem': receita.imagem.url if receita.imagem else '',
            'ingredients': [{'ingrediente_nome': ri.ingrediente.nome, 'quantidade': ri.quantidade}
                            for ri in ReceitaIngrediente.objects.filter(receita=receita)]
        }
        receitas_data.append(receita_data)

    return Response(receitas_data)


@api_view(['GET'])
def receita_detail(request, id):
    try:
        receita = Receita.objects.get(pk=id)
    except Receita.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    receita_data = {
        'user': receita.user.username if receita.user else '',
        'category': receita.category.name if receita.category else '',
        'name': receita.name,
        'description': receita.description,
        'tempoPreparacao': receita.tempoPreparacao,
        'tempoCozinhar': receita.tempoCozinhar,
        'quantidadePessoas': receita.quantidadePessoas,
        'nivel': receita.nivel,
        'imagem': receita.imagem.url if receita.imagem else '',
        'ingredients': [{'ingrediente_nome': ri.ingrediente.nome, 'quantidade': ri.quantidade}
                        for ri in ReceitaIngrediente.objects.filter(receita=receita)]
    }

    return Response(receita_data)

@api_view(['PUT'])
def update_receita(request, id):
    try:
        receita = Receita.objects.get(pk=id)
    except Receita.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # Atualiza os campos da receita com os dados da requisição
    receita.user = request.data.get('user', receita.user)
    receita.category = request.data.get('category', receita.category)
    receita.name = request.data.get('name', receita.name)
    receita.description = request.data.get('description', receita.description)
    receita.tempoPreparacao = request.data.get('tempoPreparacao', receita.tempoPreparacao)
    receita.tempoCozinhar = request.data.get('tempoCozinhar', receita.tempoCozinhar)
    receita.quantidadePessoas = request.data.get('quantidadePessoas', receita.quantidadePessoas)
    receita.nivel = request.data.get('nivel', receita.nivel)

    # Salva a receita atualizada
    receita.save()

    # Retorna os dados da receita atualizados
    receita_data = {
        'user': receita.user.username if receita.user else '',
        'category': receita.category.name if receita.category else '',
        'name': receita.name,
        'description': receita.description,
        'tempoPreparacao': receita.tempoPreparacao,
        'tempoCozinhar': receita.tempoCozinhar,
        'quantidadePessoas': receita.quantidadePessoas,
        'nivel': receita.nivel,
        'imagem': receita.imagem.url if receita.imagem else '',
        'ingredients': [{'ingrediente_nome': ri.ingrediente.nome, 'quantidade': ri.quantidade}
                        for ri in ReceitaIngrediente.objects.filter(receita=receita)]
    }

    return Response(receita_data)

@api_view(['DELETE'])
def delete_receita(request, id):
    try:
        receita = Receita.objects.get(pk=id)
    except Receita.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    receita.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

################################## FILTRAR RECEITAS ##############################################

""" @api_view(['GET'])
def filtrar_receitas(request):
    # Obter os parâmetros de consulta da solicitação
    nome_receita = request.GET.get('nome_receita', '')
    nome_categoria = request.GET.get('nome_categoria', '')

    # Inicializar a query de filtragem
    query = Q()

    # Adicionar cláusulas de filtro conforme necessário
    if nome_receita:
        query &= Q(name__icontains=nome_receita)
    if nome_categoria:
        query &= Q(category__name__icontains=nome_categoria)

    # Filtrar as receitas com base nos parâmetros
    receitas = Receita.objects.filter(query)

    # Serializar os dados das receitas filtradas
    receitas_data = []
    for receita in receitas:
        receita_data = {
            'user': receita.user.username if receita.user else '',
            'category': receita.category.name if receita.category else '',
            'name': receita.name,
            'description': receita.description,
            'tempoPreparacao': receita.tempoPreparacao,
            'tempoCozinhar': receita.tempoCozinhar,
            'quantidadePessoas': receita.quantidadePessoas,
            'nivel': receita.nivel,
            'imagem': receita.imagem.url if receita.imagem else '',
            'ingredients': [{'ingrediente_nome': ri.ingrediente.nome, 'quantidade': ri.quantidade}
                            for ri in ReceitaIngrediente.objects.filter(receita=receita)]
        }
        receitas_data.append(receita_data)

    return Response(receitas_data) """

@api_view(['GET'])
def filtrar_receitas(request):
    # Obter os parâmetros de consulta da solicitação
    nome_receita = request.GET.get('nome_receita', '')
    nome_categoria = request.GET.get('nome_categoria', '')

    # Inicializar a lista de condições de filtro
    conditions = []

    # Adicionar condições de filtro conforme necessário
    if nome_receita:
        conditions.append(Q(name__icontains=nome_receita))
    if nome_categoria:
        conditions.append(Q(category__name__icontains=nome_categoria))

    # Aplicar todas as condições de filtro usando o operador OR
    if conditions:
        receitas = Receita.objects.filter(*conditions)
    else:
        # Se não houver condições, retorne todas as receitas
        receitas = Receita.objects.all()

    # Serializar os dados das receitas filtradas
    receitas_data = []
    for receita in receitas:
        receita_data = {
            'user': receita.user.username if receita.user else '',
            'category': receita.category.name if receita.category else '',
            'name': receita.name,
            'description': receita.description,
            'tempoPreparacao': receita.tempoPreparacao,
            'tempoCozinhar': receita.tempoCozinhar,
            'quantidadePessoas': receita.quantidadePessoas,
            'nivel': receita.nivel,
            'imagem': receita.imagem.url if receita.imagem else '',
            'ingredients': [{'ingrediente_nome': ri.ingrediente.nome, 'quantidade': ri.quantidade}
                            for ri in ReceitaIngrediente.objects.filter(receita=receita)]
        }
        receitas_data.append(receita_data)

    # Verifique se há resultados e retorne uma resposta JSON
    if receitas_data:
        return Response(receitas_data)
    else:
        return JsonResponse({'message': 'Nenhuma receita encontrada.'}, status=404)


################################## ASSOCIAÇÃO: RECEITA/INGREDIENTE ##############################################

@api_view(['GET'])
def receita_ingredientes(request):
    if request.method == 'GET':
        receita_ingredientes = ReceitaIngrediente.objects.all()
        serializer = ReceitaIngredienteSerializer(receita_ingredientes, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def  create_receita_ingredientes(request):
        serializer = ReceitaIngredienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def detail_receita_ingredientes(request):
    receita_ingredientes = ReceitaIngrediente.objects.all()
    serializer = ReceitaIngredienteSerializer(receita_ingredientes, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def update_receita_ingredientes(request, id):
    try:
        receita_ingredientes = ReceitaIngrediente.objects.get(pk=id)
    except ReceitaIngrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ReceitaIngredienteSerializer(receita_ingredientes, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_receita_ingredientes(request, id):
    try:
        receita_ingredientes = ReceitaIngrediente.objects.get(pk=id)
    except ReceitaIngrediente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    receita_ingredientes.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


################################## AVALIAÇÕES ##############################################
    
@api_view(['GET'])
def avaliacoes(request):
    if request.method == 'GET':
        avaliacoes = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_avaliacoes(request):
        serializer = AvaliacaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def avaliacao_detail(request, pk):
    try:
        avaliacao = Avaliacao.objects.get(pk=pk)
    except Avaliacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AvaliacaoSerializer(avaliacao)
    return Response(serializer.data)

@api_view(['PUT'])
def update_avaliacao(request, pk):
    try:
        avaliacao = Avaliacao.objects.get(pk=pk)
    except Avaliacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = AvaliacaoSerializer(avaliacao, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def delete_avaliacao(request, pk):
    try:
        avaliacao = Avaliacao.objects.get(pk=pk)
    except Avaliacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    avaliacao.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


################################## FRIGORÍFICO ##############################################
    
@api_view(['GET'])
def frigorificos(request):
    if request.method == 'GET':
        frigorificos = Frigorifico.objects.all()
        serializer = FrigorificoSerializer(frigorificos, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_frigorifico(request):
        serializer = FrigorificoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def frigorifico_detail(request, pk):
    try:
        frigorifico = Frigorifico.objects.get(pk=pk)
    except Frigorifico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FrigorificoSerializer(frigorifico)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_frigorifico(request, pk):
    try:
        frigorifico = Frigorifico.objects.get(pk=pk)
    except Frigorifico.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    frigorifico.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

################################## FAVORITOS ##############################################
    
@api_view(['GET'])
def favoritos(request):
    if request.method == 'GET':
        favoritos = Favoritos.objects.all()
        serializer = FavoritosSerializer(favoritos, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_favoritos(request):
        serializer = FavoritosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def favoritos_detail(request, pk):
    try:
        favoritos = Favoritos.objects.get(pk=pk)
    except Favoritos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = FavoritosSerializer(favoritos)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_favoritos(request, pk):
    try:
        favoritos = Favoritos.objects.get(pk=pk)
    except Favoritos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    favoritos.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

################################## LISTA DE COMPRAS ##############################################
    
@api_view(['GET'])
def listas_compras(request):
    if request.method == 'GET':
        listas_compras = ListaCompras.objects.all()
        serializer = ListaComprasSerializer(listas_compras, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_listas_compras(request):
        serializer = ListaComprasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def lista_compras_detail(request, pk):
    try:
        lista_compras = ListaCompras.objects.get(pk=pk)
    except ListaCompras.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ListaComprasSerializer(lista_compras)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_lista_compras(request, pk):
    try:
        lista_compras = ListaCompras.objects.get(pk=pk)
    except ListaCompras.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    lista_compras.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


#################################################### UTILIZADORES ####################################################
class ProfileView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user) #cria token
        return Response({
            'token': token.key,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'user_id': user.pk,
            'email': user.email,

        })