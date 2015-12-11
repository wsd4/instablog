from django.conf.urls import url

from .views import index
from .views import list_posts
from .views import view_post
from .views import create_post
from .views import edit_post
from .views import delete_post


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^posts/$', list_posts, name='list_posts'),
    url(r'^posts/(?P<pk>[0-9]+)/$', view_post, name='view_post'),
    url(r'^posts/create/$', create_post, name='create_post'),
    url(r'^posts/(?P<pk>[0-9]+)/edit/$', edit_post, name='edit_post'),
    url(r'^posts/(?P<pk>[0-9]+)/delete/$', delete_post, name='delete_post')
]