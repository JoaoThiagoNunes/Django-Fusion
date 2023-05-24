
from django.views.generic import TemplateView

#IMPORT PARA FUNCIONAR ENVIO DE EMAIL E MENSAGEM DE SUCESSFUL
from django.urls import reverse_lazy



from .models import Servico, Funcionario, Recurso, Plano, Feedback

class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index')#quando o email for enviado, volta para essa página

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) # recupera o contexto 
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.all()   
        context['recursos'] = Recurso.objects.order_by('?').all()
        context['planos'] = Plano.objects.order_by('id')
        context['testemunhas'] = Feedback.objects.order_by('?').all()
        return context
    
    
