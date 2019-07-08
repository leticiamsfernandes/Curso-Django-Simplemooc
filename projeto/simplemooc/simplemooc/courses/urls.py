from django.conf.urls import patterns, include, url

#URL's do sistema
urlpatterns = patterns('simplemooc.courses.views',
    url(r'^$', 'index', name='index'),
)