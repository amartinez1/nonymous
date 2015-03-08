from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('confess.urls')),
    url(r'^', include('likes.urls')),
    url(r'^admin/', include(admin.site.urls)),
)