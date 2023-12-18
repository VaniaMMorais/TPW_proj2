from django.urls import path, re_path

from app import views

from django.conf import settings
from django.conf.urls.static import static


from app.views import create_ingredient, ingredient_detail, ingredientes



urlpatterns = [
    path('', views.ingredientes),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
