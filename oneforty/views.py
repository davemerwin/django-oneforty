from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from oneforty.models import Update

@login_required
def oneforty_update(request, username):
    """
    Create the actual update
    """
    
def oneforty_reply(request, username, id):
    """
    Create a reply
    """
    
def oneforty_list_all(request):
    """
    Get all of the updates
    """
    return object_list(
    request,
    Update.objects.all(),
    paginate_by=25,
    template_name='oneforty/oneforty_list_all.html',
    allow_empty=True
    )
    
def oneforty_user_list(request, username):
    """
    Get all the updates for a user
    """
    return object_list(
    request,
    Update.objects.filter(username=user.username),
    paginate_by=25,
    template_name='oneforty/oneforty_username_list_all.html',
    allow_empty=True
    )
    
def oneforty_update_detail(request, username, id):
    """
    The permalink for an update
    """