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
    
def oneforty_user_list(request, username):
    """
    Get all the updates for a user
    """
    
def oneforty_update_detail(request, username, id):
    """
    The permalink for an update
    """