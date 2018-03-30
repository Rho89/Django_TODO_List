from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from datetime import timedelta
from django.utils.translation import ugettext_lazy as _

# Create your models here.
    
class Todo(models.Model):
    
    name = models.CharField(max_length=100, unique=True)
    content = models.CharField(_(u'task'), max_length=255, default=0)
    is_resolved = models.BooleanField(_(u'Resolved?'), default=False)
    priority = models.IntegerField(default=1)
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __unicode__(self):
        return u'Task %s : %s' % (self.name, self.content)
