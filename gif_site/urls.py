from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'login_app.views.index'),
    (r'^login_page/$', 'login_app.views.login_page'),
    (r'^login/$', 'login_app.views.login_handler'),
    (r'^logout/$', 'login_app.views.logout_handler'),
    (r'^registration/$', 'login_app.views.registration'),
    (r'^newuser/$', 'login_app.views.newuser_handler'),
    (r'^gifs/', include('gif_app.urls')),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    
    # Examples:
    # url(r'^$', 'gif_site.views.home', name='home'),
    # url(r'^gif_site/', include('gif_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
