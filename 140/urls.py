from django.conf.urls.defaults import *
from 140.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Get ALL the updates
    url(r'^/', '140.views.list_all', name='all_updates'),
    # Get all the updates for a username
    url(r'^(?P<username>[\w-]+)/$', '140.views.user_list', name='username_updates'),
    # Get a single update
    url(r'^(?P<username>[\w-]+)/(?P<id>\d+)/$', '140.views.update_detail', name='update_detail'),
    # Create an update
    url(r'^update/', '140.views.update', name='140_update'),
)
