from django.urls import path
from .views import ListarPessoasView
from .views import CadastrarPessoaView
from .views import AlterarPessoaView
from .views import DeletarPessoaView

urlpatterns = [
    path('', ListarPessoasView.as_view(), name='index'),
    path('cadastro/', CadastrarPessoaView.as_view(), name='pessoa_cadastro'),
    path('alterar/<int:pk>', AlterarPessoaView.as_view(), name='pessoa_alterar'),
    path('deletar/<int:pk>', DeletarPessoaView.as_view(), name='pessoa_deletar'),

]