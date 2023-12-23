from rest_framework import serializers
from app.models import *

#################################################### INGREDIENTES ####################################################

class CategoriaIngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoriaIngrediente
        fields = '__all__'


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

class ReceitaIngredienteSerializer(serializers.ModelSerializer):
    ingrediente_nome = serializers.SerializerMethodField()  # Adicionando um campo para o nome do ingrediente

    class Meta:
        model = ReceitaIngrediente
        fields = '__all__'

    def get_ingrediente_nome(self, obj):
        return obj.nome  # Obtendo o nome do ingrediente


class ReceitaSerializer(serializers.ModelSerializer):
    category = CategoriaSerializer()
    ingredients = ReceitaIngredienteSerializer(many=True, read_only=True)  # Alteração aqui
    imagem = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = Receita
        fields = ('user', 'category', 'name', 'description', 'tempoPreparacao', 'tempoCozinhar', 'quantidadePessoas', 'nivel', 'imagem', 'ingredients', 'updated', 'created')

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        category_instance = Categoria.objects.create(**category_data)
        ingredients_data = validated_data.pop('ingredients') if 'ingredients' in validated_data else None

        receita_instance = Receita.objects.create(category=category_instance, **validated_data)

        # Adiciona os ingredientes à receita
        if ingredients_data:
            for ingrediente_data in ingredients_data:
                ingrediente_serializer = ReceitaIngredienteSerializer(data=ingrediente_data)
                if ingrediente_serializer.is_valid():
                    ingrediente_serializer.save(receita=receita_instance)
                else:
                    raise serializers.ValidationError(ingrediente_serializer.errors)

        return receita_instance

    def update(self, instance, validated_data):
        category_data = validated_data.pop('category', None)
        ingredients_data = validated_data.pop('ingredients', None)

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.tempoPreparacao = validated_data.get('tempoPreparacao', instance.tempoPreparacao)
        instance.tempoCozinhar = validated_data.get('tempoCozinhar', instance.tempoCozinhar)
        instance.quantidadePessoas = validated_data.get('quantidadePessoas', instance.quantidadePessoas)
        instance.nivel = validated_data.get('nivel', instance.nivel)

        # Atualiza a categoria, se fornecida
        if category_data:
            categoria_serializer = CategoriaSerializer(instance.category, data=category_data)
            if categoria_serializer.is_valid():
                categoria_serializer.save()
            else:
                raise serializers.ValidationError(categoria_serializer.errors)

        # Atualiza os ingredientes, se fornecidos
        if ingredients_data:
            instance.receitaingrediente_set.all().delete()
            for ingrediente_data in ingredients_data:
                ingrediente_serializer = ReceitaIngredienteSerializer(data=ingrediente_data)
                if ingrediente_serializer.is_valid():
                    ingrediente_serializer.save(receita=instance)
                else:
                    raise serializers.ValidationError(ingrediente_serializer.errors)

        # Atualiza a imagem, se fornecida
        if 'imagem' in validated_data:
            instance.imagem = validated_data.get('imagem', instance.imagem)

        instance.save()
        return instance


################################## ASSOCIAÇÃO: RECEITA/INGREDIENTE ##############################################

""" class ReceitaIngredienteSerializer(serializers.ModelSerializer):
    
    ingrediente_nome = serializers.SerializerMethodField()  # Adicionando um campo para o nome do ingrediente

    class Meta:
        model = ReceitaIngrediente
        fields = '__all__'

    def get_ingrediente_nome(self, obj):
        return obj.nome  # Obtendo o nome do ingrediente
    
    def create(self, validated_data):
        receita = validated_data.pop('receita')
        ingrediente = validated_data.pop('ingrediente')

        receita_ingrediente_instance = ReceitaIngrediente.objects.create(receita=receita, ingrediente=ingrediente, **validated_data)
        return receita_ingrediente_instance
    
    def update(self, instance, validated_data):
        instance.quantidade = validated_data.get('quantidade', instance.quantidade)
        instance.unidade = validated_data.get('unidade', instance.unidade)
        instance.save()
        return instance """
    
""" class ReceitaIngredienteSerializer(serializers.ModelSerializer):
 
    ingrediente_nome = serializers.SerializerMethodField()

    class Meta:
        model = ReceitaIngrediente
        fields = '__all__'

    def get_ingrediente_nome(self, obj):
        return obj.ingrediente.nome

    def create(self, validated_data):
        return super().create(validated_data, receita=validated_data['receita'])

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
 """


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