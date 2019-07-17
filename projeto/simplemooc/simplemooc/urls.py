from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

#URL's do sistema
urlpatterns = patterns('',
    #Na primeira diz que para uma url vazia, execute a 
    #função simplemooc.core.views.home e seu nome é home
    #o 'name' é o nome da url
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^cursos/', include('simplemooc.courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
)

#se estiver no modo de desenvolvimento
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
