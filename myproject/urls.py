from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL}),
    url(r'^annotated/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL}),
    url(r'^annotated$', "cms_users_templates.views.dispositivosPlantilla"),
    url(r'^annotated/(.*)$', "cms_users_templates.views.elementoPlantilla"),
    url(r'^dispositivos$', "cms_users_templates.views.dispositivos"),
    url(r'^dispositivos/(.*)$', "cms_users_templates.views.info"),
    url(r'^(.*)$', "cms_users_templates.views.notFound"),
    
)
