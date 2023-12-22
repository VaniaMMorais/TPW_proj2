from rest_framework import serializers
from app.models import *

#################################################### INGREDIENTES ####################################################

class CategoriaIngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriaIngrediente
        fields = '__all__'

# class IngredienteSerializer(serializers.ModelSerializer):

#     categoria = CategoriaIngredienteSerializer()
    
#     class Meta:
#         model = Ingrediente
#         fields = ('nome', 'categoria','icon', 'calorias')
class IngredienteSerializer(serializers.ModelSerializer):
    categoria = CategoriaIngredienteSerializer()

    class Meta:
        model = Ingrediente
        fields = ('id','nome', 'categoria', 'icon', 'calorias')

    def create(self, validated_data):
        categoria_data = validated_data.pop('categoria')
        categoria_instance = CategoriaIngrediente.objects.create(**categoria_data)

        ingrediente_instance = Ingrediente.objects.create(categoria=categoria_instance, **validated_data)
        return ingrediente_instance
    
    def update(self, instance, validated_data):
        categoria_data = validated_data.pop('categoria', None)
        
        instance.nome = validated_data.get('nome', instance.nome)
        instance.icon = validated_data.get('icon', instance.icon)
        instance.calorias = validated_data.get('calorias', instance.calorias)

        # Atualiza a categoria, se fornecida
        if categoria_data:
            categoria_serializer = CategoriaIngredienteSerializer(instance.categoria, data=categoria_data)
            if categoria_serializer.is_valid():
                categoria_serializer.save()
            else:
                raise serializers.ValidationError(categoria_serializer.errors)

        instance.save()
        return instance


#################################################### RECEITAS ####################################################
        
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = ('user', 'category', 'name', 'description', 'tempoPreparacao', 'tempoCozinhar', 'quantidadePessoas', 'nivel', 'imagem', 'ingredients', 'updated', 'created')
    imagem = serializers.StringRelatedField(read_only=True)


################################## ASSOCIAÇÃO: RECEITA/INGREDIENTE ##############################################

class ReceitaIngredienteSerializer(serializers.ModelSerializer):
    ingrediente_nome = serializers.SerializerMethodField()  # Adicionando um campo para o nome do ingrediente

    class Meta:
        model = ReceitaIngrediente
        fields = '__all__'

    def get_ingrediente_nome(self, obj):
        return obj.ingrediente.nome  # Obtendo o nome do ingrediente


################################## AVALIAÇÕES ##############################################
        
class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('user', 'receita', 'descricao', 'clasificacao', 'data', 'updated', 'created')


################################## FRIGORÍFICO ##############################################
        
class FrigorificoSerializer(serializers.ModelSerializer):
    class Meta:

        model = Frigorifico
        fields = ('user', 'ingredient', 'data', 'checklist', 'updated', 'created')



################################## FAVORITOS ############################################## 

class FavoritosSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model = Favoritos
        fields = ('user', 'receita', 'updated', 'created')

################################## LISTA DE COMPRAS ##############################################

class ListaComprasSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListaCompras
        fields = ('user', 'ingredient', 'data', 'checklist')

################################## USER ##############################################

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =('id', 'username', 'first_name', 'last_name', 'email')