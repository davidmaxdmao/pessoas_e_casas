from django.urls import path
from .views import ListarCasasView
from .views import CadastrarCasaView
from .views import AlterarCasaView
from .views import DeletarCasaView

urlpatterns = [
    path('', ListarCasasView.as_view(), name='listar_casa'),
    path('cadastro/', CadastrarCasaView.as_view(), name='cadastrar_casa'),
    path('alterar/<int:pk>', AlterarCasaView.as_view(), name='alterar_casa'),
    path('deletar/<int:pk>', DeletarCasaView.as_view(), name='deletar_casa'),
]
