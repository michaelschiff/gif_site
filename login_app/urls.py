from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('login_app.views',
    (r'^$', 'index'),
    (r'^login_page/$', 'login_page'),
    (r'^login/$', 'login_handler'),
    (r'^logout/$', 'logout_handler'),
    (r'^registration/$', 'registration'),
    (r'^newuser/$', 'newuser_handler'),
)
