from django.urls import path
from .views import ListarCasasView

urlpatterns = [
    path('', ListarCasasView.as_view(), name='listar_casa'),
]
