from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
     (r'^news/', include("news.urls")),
     (r'^zk /', include('django.contrib.admin.urls')),

)