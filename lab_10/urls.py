from django.conf.urls import url
from .views import *

from .custom_auth import auth_login, auth_logout

urlpatterns = [
    # custom auth
    url(r'^custom_auth/login/$', auth_login, name='auth_login'),
    url(r'^custom_auth/logout/$', auth_logout, name='auth_logout'),

    # index dan dashboard
    url(r'^$', index, name='index'),
    url(r'^dashboard/$', dashboard, name='dashboard'),

    #movie
    url(r'^movie/list/$', movie_list, name='movie_list'),
    url(r'^movie/detail/(?P<id>.*)/$', movie_detail, name='movie_detail'),

    # Session dan Model (Watch Later)
    url(r'^movie/watch_later/add/(?P<id>.*)/$', add_watch_later, name='add_watch_later'),
    url(r'^movie/watch_later/$', list_watch_later, name='list_watch_later'),

    #API
    url(r'^api/movie/(?P<judul>.*)/(?P<tahun>.*)/$', api_search_movie, name='api_search_movie'),
]
