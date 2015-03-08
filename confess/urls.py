from django.conf.urls import patterns, url
from .views import PostListView,ConfessForm,PostDetailView, newList,popularList

urlpatterns = patterns('',
    
    url(r'^$',PostListView.as_view(), name = 'list'),
    url(r'^list/$',PostListView.as_view()),
    # url(r'^confessions/$',postList, name = 'list'),
    url(r'^form/$',ConfessForm.as_view(), name='form'),
    url(r"^confessions/(?P<slug>[^\.]+)/$", PostDetailView.as_view(), name = 'detail'),
    url(r'^new/$',newList,name='new'),
    url(r'^popular/$',popularList,name='popular'),

)