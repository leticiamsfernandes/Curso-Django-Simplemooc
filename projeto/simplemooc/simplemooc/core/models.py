from django.db import models

# Create your models here.
class Course(models.Model):
	#CharField = campo do tipo char
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')

	#TextField = não possui tamanho máximo
	#blank = campo não obrigatório
	descrption = models.TextField('Descrição', blank=True)

	#null = indica que no banco de dados ele pode ser null
	start_date = models.DateField('Data de Início', null=True, blank=True)

	#campo do tipo imagem = campo do tipo texto com o caminho da imagem
	#o django salva imagens no diretório físico
	#upload_to = caminho no qual o django irá salvar a imagem, necessita de um settings chamado MEDIA_ROOT
	image = models.ImageField(upload_to='courses/images', verbose_name='Imagem')

	#tipo DateTimeField é data/hora, diferente de DateField
	created_at = models.DateTimeField('Criado em', auto_now_add=True)

	updated_at = models.DateTimeField('Atualizado em', auto_now=True)