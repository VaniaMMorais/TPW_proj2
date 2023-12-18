from django.contrib import admin

from .models import Receita,Categoria,Avaliacao,Ingrediente,ReceitaIngrediente,Frigorifico,Favoritos,ListaCompras,CategoriaIngrediente

admin.site.register(Receita)
admin.site.register(Categoria)
admin.site.register(CategoriaIngrediente)   
admin.site.register(Avaliacao)                   
admin.site.register(Ingrediente)  
admin.site.register(ReceitaIngrediente)  
admin.site.register(Frigorifico)  
admin.site.register(Favoritos)  
admin.site.register(ListaCompras)  