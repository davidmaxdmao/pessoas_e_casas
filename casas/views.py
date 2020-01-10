from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView

from .models import Casa
from .forms import CasaForm



class ListarCasasView(ListView):
    model = Casa
    template_name = 'casas/index.html'
    form_class = CasaForm


class CadastrarCasaView(CreateView):
    model = Casa
    template_name = 'casas/cadastro.html'
    form_class = CasaForm
    success_url = reverse_lazy('listar_casa')


class AlterarCasaView(UpdateView):
    model = Casa
    template_name = 'casas/cadastro.html'
    form_class = CasaForm
    success_url = reverse_lazy('listar_casa')


class DeletarCasaView(DeleteView):
    model = Casa
    template_name = 'casas/deletar.html'
    success_url = reverse_lazy('listar_casa')








