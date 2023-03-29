from rest_framework import viewsets
from .serializer import JogoSerializer, LojaSerializer
from .models import Jogo, Loja

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class LojaViewSet(viewsets.ModelViewSet):
    queryset = Loja.objects.all()
    serializer_class = LojaSerializer