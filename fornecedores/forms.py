import re

from django import forms

from .models import Fornecedor


class FornecedorModelForm(forms.ModelForm):
    def clean_cnpj(self):
        cnpj = self.cleaned_data.get('cnpj')
        cnpj_aux = re.sub(r'\D', '', cnpj)  # Remove caracteres não numéricos
        if len(cnpj_aux) != 14:
            raise forms.ValidationError("CNPJ deve conter 14 números.")
        return cnpj

    class Meta:
        model = Fornecedor
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do fornecedor é um campo obrigatório'},
            'cnpj': {'required': 'O cnpj do fornecedor é um campo obrigatório', 'unique': 'Cnpj já cadastrado'},
            'fone': {'required': 'O número do telefone é um campo obrigatório'},
        }