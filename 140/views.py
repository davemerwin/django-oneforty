from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from 140.models import Update

@login_required
def update(request, username):
    """
    Create the actual update
    """
    
def list_all(request):
    """
    Get all of the updates
    """
    
def user_list(request, username):
    """
    Get all the updates for a user
    """
    
def update_detail(request, username, id):
    """
    The permalink for an update
    """