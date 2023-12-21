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
from app.views import create_ingredient, ingredient_detail, ingredientes, create_receita,receitas,receita_detail,avaliacao_detail,avaliacoes,categorias,categoria_detail,categoria_ingredientes,categoria_ingrediente_detail,receita_ingredientes,receita_ingrediente_detail, frigorificos,frigorifico_detail,favoritos,favoritos_detail,listas_compras,lista_compras_detail
urlpatterns = [

    path('accounts/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('ingredientes/', views.ingredientes),
    path('criarIngrediente/', views.create_ingredient),
    path('ingredientes/<int:id>', views.ingredient_detail),

    path('receitas/', views.receitas),
    path('criarReceita/', views.create_receita),
    path('receitas/<int:id>', views.receita_detail),

    path('categorias/', views.categorias),
    path('categorias/<int:pk>/', views.categoria_detail),

    path('categoria-ingredientes/', views.categoria_ingredientes),
    path('categoria-ingredientes/<int:pk>/', views.categoria_ingrediente_detail),

    path('receita_ingredientes/', views.receita_ingredientes),
    path('receita_ingredientes/<int:pk>/', views.receita_ingrediente_detail),

    path('avaliacoes/', avaliacoes),
    path('avaliacoes/<int:pk>/', avaliacao_detail),

    path('frigorificos/', frigorificos),
    path('frigorificos/<int:pk>/', frigorifico_detail),

    path('favoritos/', favoritos),
    path('favoritos/<int:pk>/', favoritos_detail),

    path('listas_compras/', listas_compras),
    path('listas_compras/<int:pk>/', lista_compras_detail),



    path('', include('app.urls')),
    
]
