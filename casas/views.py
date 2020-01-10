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



