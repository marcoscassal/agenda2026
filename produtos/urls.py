from django.urls import path

from .views import ProdutosView, ProdutoAddView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('produtos/', ProdutosView.as_view(), name='produtos'),
    path('produtos/novo/', ProdutoAddView.as_view(), name='produto_adicionar'),
    path('produtos/<int:pk>/editar/', ProdutoUpdateView.as_view(), name='produto_editar'),
    path('produtos/<int:pk>/apagar/', ProdutoDeleteView.as_view(), name='produto_apagar'),
]