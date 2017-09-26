from django.conf.urls import url
from .views import index, add_message


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^add_message', message_post, name='add_message'),

]
