from django.conf.urls import patterns, include, url

#URL's do sistema
urlpatterns = patterns('simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
    #mostra a primary key inteiro
    #url(r'^(?P<pk>\d+)/$', 'details', name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', 'details', name='details'),
)