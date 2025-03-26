from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categorias', CategoriaViewSet, basename='categorias')
router.register('produtos', ProdutoViewSet, basename='produtos')
urlpatterns = router.urls

# urlpatterns = [
#     path('', home)
# ]