from django.urls import path, re_path

from app import views
from .views import create_ingredient, delete_ingredient, ingredient_detail, update_ingredient

from django.conf import settings
from django.conf.urls.static import static


from app.views import create_ingredient, delete_ingredient, ingredient_detail, update_ingredient

urlpatterns = [
    path('ingredientes/', create_ingredient, name='create_ingredient'),
    path('ingredientes/<int:ing_id>/', delete_ingredient, name='delete_ingredient'),
    path('ingredientes/<int:ing_id>/', ingredient_detail, name='ingredient_detail'),
    path('ingredientes/<int:ing_id>/update/', update_ingredient, name='update_ingredient'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
