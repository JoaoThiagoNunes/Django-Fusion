from typing import Any, Dict
from django.views.generic import FormView

#IMPORT PARA FUNCIONAR ENVIO DE EMAIL E MENSAGEM DE SUCESSFUL
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm

from .models import Servico, Funcionario, Recurso, Plano, Feedback

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')#quando o email for enviado, volta para essa página

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) # recupera o contexto 
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()   
        context['recursos'] = Recurso.objects.order_by('?').all()
        context['planos'] = Plano.objects.order_by('id')
        context['testemunhas'] = Feedback.objects.order_by('?').all()
        return context
    
    def form_valid(self, form, *args, **kwargs):
        print('-'*80)
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form,*args, **kwargs)
    
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)

