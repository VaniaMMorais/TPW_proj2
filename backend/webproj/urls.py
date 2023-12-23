"""
URL configuration for webproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app import views

from django.urls import path, include



urlpatterns = [

    path('accounts/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('ingredientes/', views.ingredientes),
    path('criarIngrediente/', views.create_ingredient),
    path('ingredientes/<int:id>', views.get_ingredient_detail),
    path('update_ingrediente/<int:id>', views.update_ingredient),
    path('delete_ingrediente/<int:id>', views.delete_ingredient),

    path('receitas/', views.receitas),
    path('criarReceita/', views.create_receita),
    path('detail_receita/<int:id>', views.receita_detail),
    path('update_receita/<int:id>', views.update_receita),
    path('delete_receita/<int:id>', views.delete_receita),
    path('receitas_filtradas/', views.filtrar_receitas),

    path('categorias/', views.categorias),
    path('criarCategoria/', views.create_categoria),
    path('categorias/<int:pk>/', views.categoria_detail),
    path('categorias/<int:pk>/', views.edit_categoria),
    path('categorias/<int:pk>/', views.delete_categoria),

    path('categoria-ingredientes/', views.all_categoria_ingredientes),
    path('create_categoria_ingrediente/', views.create_categoria_ingrediente),
    path('categoria-ingredientes/<int:pk>/', views.categoria_ingrediente_detail),
    path('edit_categoria-ingredientes/<int:pk>/', views.edit_categoria_ingrediente),
    path('delete_categoria-ingredientes/<int:pk>/', views.delete_categoria_ingrediente),


    path('receita_ingredientes/', views.receita_ingredientes),
    path('create_receita_ingredientes/', views.create_receita_ingredientes),
    path('detail_receita_ingredientes/<int:pk>/', views.detail_receita_ingredientes),
    path('update_receita_ingredientes/<int:pk>/', views.update_receita_ingredientes),
    path('delete_receita_ingredientes/<int:pk>/', views.delete_receita_ingredientes),

    path('avaliacoes/', views.avaliacoes),
    path('criarAvaliacao/', views.create_avaliacoes),
    path('detail_avaliacoes/<int:pk>/', views.avaliacao_detail),
    path('update_avaliacoes/<int:pk>/', views.update_avaliacao),
    path('remove_avaliacoes/<int:pk>/', views.delete_avaliacao),

    path('frigorificos/', views.frigorificos),
    path('add_frigorifico/', views.create_frigorifico),
    path('detail_frigorifico/<int:pk>/', views.frigorifico_detail),
    path('remove_frigorifico/<int:pk>/', views.delete_frigorifico),

    path('favoritos/', views.favoritos),
    path('add_favoritos/', views.create_favoritos),
    path('detail_favoritos/<int:pk>/', views.favoritos_detail),
    path('remove_favoritos/<int:pk>/', views.delete_favoritos),

    path('listas_compras/', views.listas_compras),
    path('add_lista_compras/', views.create_listas_compras),
    path('listas_compras/<int:pk>/', views.lista_compras_detail),
    path('remove_lista_compras/<int:pk>/', views.delete_lista_compras),

    path('', include('app.urls')),
    
]

