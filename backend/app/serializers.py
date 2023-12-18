from rest_framework import serializers
from app.models import *

#################################################### INGREDIENTES ####################################################

class CategoriaIngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriaIngrediente
        fields = ('nome')

class IngredienteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Ingrediente
        fields = ('nome', 'categoria','icon', 'calorias')


#################################################### RECEITAS ####################################################
        
class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('name')


class ReceitaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Receita
        fields = ('user', 'categoria', 'category','name', 'description', 'tempoPreparacao', 'tempoCozinhar', 'quantidadePessoas', 'nivel', 'imagem', 'ingredients', 'updated', 'created')
    imagem = serializers.StringRelatedField(read_only=True)


################################## ASSOCIAÇÃO: RECEITA/INGREDIENTE ##############################################
        
class ReceitaIngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReceitaIngrediente
        fields = ('receita', 'ingrediente', 'quantidade')


################################## AVALIAÇÕES ##############################################
        
class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avaliacao
        fields = ('user', 'receita', 'rating', 'updated', 'created')


################################## FRIGORÍFICO ##############################################
        
class FrigorificoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Frigorifico
        fields = ('user', 'ingrediente', 'quantidade', 'updated', 'created')


################################## FAVORITOS ############################################## 

class FavoritosSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Favoritos
        fields = ('user', 'receita', 'updated', 'created')

################################## LISTA DE COMPRAS ##############################################

class ListaComprasSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ListaCompras
        fields = ('user', 'ingrediente', 'quantidade', 'updated', 'created')