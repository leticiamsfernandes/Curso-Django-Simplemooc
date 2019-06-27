from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#URL's do sistema
urlpatterns = patterns('',
    #Na primeira diz que para uma url vazia, execute a 
    #função simplemooc.core.views.home e seu nome é home
    url(r'^$', 'simplemooc.core.views.home', name='home'),
    url(r'^contato/$', 'simplemooc.core.views.contact', name='contact'),
    url(r'^admin/', include(admin.site.urls)),
)
