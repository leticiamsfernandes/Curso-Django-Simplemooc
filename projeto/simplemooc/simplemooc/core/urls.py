from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

#URL's do sistema
urlpatterns = patterns('simplemooc.core.views',
    url(r'^$', 'home', name='home'),
    url(r'^contato/$', 'contact', name='contact'),
)
