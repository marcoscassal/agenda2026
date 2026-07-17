from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ProdutoModelForm
from .models import Produto


class ProdutosView(ListView):
    model = Produto
    template_name = 'produtos.html'
    context_object_name = 'produtos'
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset().select_related('fornecedor')
        buscar = self.request.GET.get('buscar')
        if buscar:
            queryset = queryset.filter(nome__icontains=buscar)
        return queryset


class ProdutoAddView(SuccessMessageMixin, CreateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'produto_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto cadastrado com sucesso!'


class ProdutoUpdateView(SuccessMessageMixin, UpdateView):
    model = Produto
    form_class = ProdutoModelForm
    template_name = 'Produto_form.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto alterado com sucesso!'


class ProdutoDeleteView(SuccessMessageMixin, DeleteView):
    model = Produto
    template_name = 'produto_apagar.html'
    success_url = reverse_lazy('produtos')
    success_message = 'Produto apagado com sucesso!'
