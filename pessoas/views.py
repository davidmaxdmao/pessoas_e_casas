from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from .models import Pessoa
from .forms import PessoaForm

# Create your views here.

class ListarPessoasView(ListView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoas/index.html'


class CadastrarPessoaView(CreateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoas/cadastro.html'
    success_url = reverse_lazy('index')

class AlterarPessoaView(UpdateView):
    model = Pessoa
    form_class = PessoaForm
    template_name = 'pessoas/cadastro.html'
    success_url = reverse_lazy('index')


class DeletarPessoaView(DeleteView):
    model = Pessoa
    template_name = 'pessoas/deletar.html'
    success_url = reverse_lazy('index')


