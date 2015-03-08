from django.conf.urls import patterns,url
from .views import retrieve_token, like, unlike, like_count, fill_modal, user_like


urlpatterns = patterns('',

                       url(r'^getCookie/$', retrieve_token, name='token'),
                       url(r'^like/$', like.as_view(), name='like'),
                       url(r'^unlike/$', unlike, name='unlike'),
                       url(r'^like_count/$', like_count, name='like_count'),
                       url(r'^fill/$', fill_modal.as_view(), name='fill'),
                       url(r'^label/$', user_like.as_view(), name='label'),
                       )
