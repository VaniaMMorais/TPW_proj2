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
from app.views import ingredientes,create_ingredient,get_ingredient_detail,update_ingredient,delete_ingredient
from app.views import create_receita,receitas,receita_detail
from app.views import avaliacao_detail,avaliacoes,categorias
from app.views import categoria_ingrediente_detail,all_categoria_ingredientes,create_categoria_ingrediente,edit_categoria_ingrediente,delete_categoria_ingrediente
from app.views import receita_ingredientes,receita_ingrediente_detail
from app.views import frigorificos,frigorifico_detail
from app.views import favoritos,favoritos_detail
from app.views import listas_compras,lista_compras_detail
from app.views import ReceitaFilterAPIView


urlpatterns = [

    path('accounts/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    # ingredientes
    path('ingredientes/', views.ingredientes),
    path('criarIngrediente/', views.create_ingredient),
    path('ingredientes/<int:id>', views.get_ingredient_detail),
    path('update_ingrediente/<int:id>', views.update_ingredient),
    path('delete_ingrediente/<int:id>', views.delete_ingredient),

    path('receitas/', views.receitas),
    path('criarReceita/', views.create_receita),
    path('receitas/<int:id>', views.receita_detail),
    path('receitas/filtradas/', ReceitaFilterAPIView.as_view()),

    path('categorias/', views.categorias),
    path('categorias/<int:pk>/', views.categoria_detail),

    # categorias dos ingredientes
    path('categoria-ingredientes/', views.all_categoria_ingredientes),
    path('create_categoria_ingrediente/', views.create_categoria_ingrediente),
    path('categoria-ingredientes/<int:pk>/', views.categoria_ingrediente_detail),
    path('edit_categoria-ingredientes/<int:pk>/', views.edit_categoria_ingrediente),
    path('delete_categoria-ingredientes/<int:pk>/', views.delete_categoria_ingrediente),

    path('receita_ingredientes/', views.receita_ingredientes),
    path('receita_ingredientes/<int:pk>/', views.receita_ingrediente_detail),

    # FUNCIONAM CORRETAMENTE (testei no postman)
    path('avaliacoes/', avaliacoes),
    path('avaliacoes/<int:pk>/', avaliacao_detail),
    
    # FUNCIONAM CORRETAMENTE (testei no postman)
    path('frigorificos/', frigorificos),
    path('frigorificos/<int:pk>/', frigorifico_detail),

    path('favoritos/', favoritos),
    path('favoritos/<int:pk>/', favoritos_detail),

    path('listas_compras/', listas_compras),
    path('listas_compras/<int:pk>/', lista_compras_detail),



    path('', include('app.urls')),
    
]
