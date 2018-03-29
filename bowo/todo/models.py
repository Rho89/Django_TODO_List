from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from datetime import timedelta

# Create your models here.
    
class todo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=False)
    priority = models.IntegerField(default=1, null=True)
    created = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return 'Profile of user: %s' % self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

