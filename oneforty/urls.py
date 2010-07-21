from django.conf.urls.defaults import *
from oneforty.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Get ALL the updates
    url(r'^/', 'oneforty.views.oneforty_list_all', name='oneforty_all_updates'),
    # Get all the updates for a username
    url(r'^(?P<username>[\w-]+)/$', 'oneforty.views.oneforty_user_list', name='oneforty_username_updates'),
    # Get a single update
    url(r'^(?P<username>[\w-]+)/(?P<id>\d+)/$', 'oneforty.views.oneforty_update_detail', name='oneforty_detail'),
    # Create an update
    url(r'^update/', 'oneforty.views.oneforty_update', name='oneforty_update'),
    # Create a reply
    url(r'^reply/', 'oneforty.views.oneforty_reply', name='oneforty_reply'),
)
