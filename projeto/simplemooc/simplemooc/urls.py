from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#URL's do sistema
urlpatterns = patterns('',
    #Na primeira diz que para uma url vazia, execute a 
    #função simplemooc.core.views.home e seu nome é home
    #o 'name' é o nome da url
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
)
