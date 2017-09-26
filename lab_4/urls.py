from django.conf.urls import url
from .views import index, message_post, message_table


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_message', message_post, name='add_message'),
    url(r'^result_table', message_table, name='result_table'),

]
