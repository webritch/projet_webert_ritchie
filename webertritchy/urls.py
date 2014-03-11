from django.conf.urls import patterns, include, url
from django.conf.urls import *

from django.contrib import admin
import django.core.handlers.wsgi
import application.views
from django.conf.urls import patterns, url

admin.autodiscover()

urlpatterns = patterns('application.views',
                              #url(r'^$', 'accueil', name='accueil'),
                              #url(r'^loginadmin$', 'FormulaireLoginAdmin'),
                              #url(r'^loginprof$', 'FormulaireLoginProf'),
                              #url(r'^CreationCompte$', 'FormulaireCompteProf'),
                              #url(r'^professeur$', 'EnregistrerProfesseur'),
                              #url(r'^log/$', 'login'),
                              #url(r'^cours$', 'CoursSauvegarde'),
                              #url(r'^descriptif$', 'coursdescriptif'),
                              #url(r'^Programme$', 'FormProg'),
                              #url(r'^lcours$', 'lcours'),
                              #url(r'^lprogramme$', 'lprogramme'),
                              #url(r'^lprofesseur$', 'lprofesseur'),
                              #url(r'^ldescriptif$', 'ldescriptif'),
                              #url(r'^web$', 'web'),
                              #url(r'^InterfaceProf$', 'InterfaceProf', name='InterfaceProf'),
                             # url(r'^home/$', 'blog.views.accueil'), chercher a comprendre pourquoi ca a donne l'erreur
                               # url(r'^blog/', include('blog.urls')),

                                # url(r'^admin/', include(admin.site.urls)),
                                # url(r'^$', 'webertritchy.views.home'),
)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
)