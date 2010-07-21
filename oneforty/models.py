from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Update(models.Model):
    """
    The update is the heart of the app. This is where the content will go. It is analogous to a status update on facebook or a tweet on twitter.
    """
    text = models.CharField(_('text'), max_length=140)
    sent = models.DateTimeField(_('sent'), default=datetime.now)
    sender = models.ForeignKey(User)
    
    def get_absolute_url(self):
        return ("single_update", [self.id])
    get_absolute_url = models.permalink(get_absolute_url)
    
    class Meta:
        ordering = ('-sent',)
        verbose_name = _('Update')
        verbose_name_plural = _('Updates')

    def __unicode__(self):
        return self.text
        
class Reply(models.Model):
    update = models.ForeignKey(Update)
    replier = models.ForeignKey(User)