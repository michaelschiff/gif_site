from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('gif_app.views',
    (r'^$', 'index'),
    (r'^newgif/$', 'newgif'),
)
