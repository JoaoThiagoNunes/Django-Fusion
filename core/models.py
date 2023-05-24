import uuid

from django.db import models

from stdimage.models import StdImageField

def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename= f'{uuid.uuid4()}.{ext}'
    return filename

class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True) #add no final indica que só colocará a data quando for criado
    modificado = models.DateField('Atualização', auto_now=True) #sem o add apenas atualiza
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Servico(Base):
    icons_choice = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Design'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    icon = models.CharField('Icone', max_length=12, choices=icons_choice) #O numero 12 foi retirado da maior tag contendo 12 caracters 
                                                                            #ref: #-----------

    class Meta: #Serve para apresentar no html o nome Serviço corretamente, senão seria Servico o nome da classe 
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.servico
    

class Cargo(Base): #criar uma classe cargo para definir quais cargos a "empresa" tem
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo
    

class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name ='Cargo', on_delete=models.CASCADE) 
    #ForeingnKey = chave estrangeira, quando coloca ela é obrigatório colocar o on_delete
    #On_delete = caso o cargo não exista mais irá excluir que possuia esse cargo
    bio = models.TextField('bio', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':480, 'height':480, 'crop':True}})
                                                                     #480x480 é igual ao tamanho do template      
    facebook = models.CharField('Facebook', max_length=100, default='#')
    twitter = models.CharField('Twitter', max_length=100, default='#')
    instagram = models.CharField('Instagram', max_length=100, default='#')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Recurso(Base):
    icons_choice = (
        ('lni-rocket', 'Foguete'),
        ('lni-laptop-phone', 'Tablet'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha' ),
        ('lni-layers', 'Camadas'),
    )

    recurso = models.CharField('Recurso', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    icon = models.CharField('Icone', max_length=16, choices=icons_choice)

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return self.recurso


class Plano(Base):
    icons_choice = (
        ('lni-package', 'Pacote'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela'),
    )

    plano = models.CharField('Plano', max_length=100)
    preco = models.CharField('Preço', max_length=100)
    descricao = models.CharField('Descrição', max_length=200)
    icon = models.CharField('Icone', max_length=12, choices=icons_choice)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.plano
    
class Feedback(Base):
    nome = models.CharField('Nome', max_length=100)
    cargo = models.ForeignKey('core.Cargo', verbose_name ='Cargo', on_delete=models.CASCADE) 
    comentario = models.CharField('Comentário', max_length=200)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb':{'width':75, 'height':75, 'crop':True}})

    class Meta:
        verbose_name = 'Feedback'
        verbose_name = 'Feedback'
    
    def __str__(self):
        return self.nome

