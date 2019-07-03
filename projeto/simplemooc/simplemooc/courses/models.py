from django.db import models

class CourseManager(models.Manager):
	#o manager tem uma querySet que representa a listagem
	#das referências dos objetos que vem do banco de dados

	def search(self, query):
		return self.get_queryset().filter(
			models.Q(name__icontains=query) | \
			models.Q(description__icontains=query) \
			)

# Create your models here.
class Course(models.Model):
	#CharField = campo do tipo char
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Atalho')

	#TextField = não possui tamanho máximo
	#blank = campo não obrigatório
	description = models.TextField('Descrição', 
		blank=True)

	#null = indica que no banco de dados ele pode ser null
	start_date = models.DateField('Data de Início', 
		null=True, blank=True)

	#campo do tipo imagem = campo do tipo texto com o caminho da imagem
	#o django salva imagens no diretório físico
	#objetos tipo image dependem de uma biblioteca chamada Pillow PARA TRATAMENTO DE IMAGENS
	#upload_to = caminho no qual o django irá salvar a imagem, necessita de um settings chamado MEDIA_ROOT
	image = models.ImageField(upload_to='courses/images', 
		verbose_name='Imagem', null=True, blank=True)

	#tipo DateTimeField é data/hora, diferente de DateField
	created_at = models.DateTimeField('Criado em', 
		auto_now_add=True)

	updated_at = models.DateTimeField('Atualizado em', 
		auto_now=True)

	#aqui é definido o .objects como não mais o padrão 
	#do django, mas sim o que foi criado na classe 
	#CourseManager()
	objects=CourseManager()

	#retorna a string contendo o nome do course
	#ao invés de "CourseObject"
	def __str__(self):
		return self.name

	class Meta:
		#opcoes meta do model que o django usa para 
		#determinados fins
		verbose_name = 'Curso'
		verbose_name_plural = 'Cursos'

		#ordering -> ordena o padrão que o Django
		#irá ordenar quando buscar as informações
		#exemplo: no admin irá aparecer por ordem 
		#ascendente de nomes
		ordering = ['name']
