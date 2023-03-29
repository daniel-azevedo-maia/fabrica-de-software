from django.contrib import admin
from django.urls import path, include
from videogame_store.views import JogoViewSet, LojaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jogos', JogoViewSet, basename='Jogos')
router.register('lojas', LojaViewSet, basename='Loja')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
