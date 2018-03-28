from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


    
class todo(models.Model):
    name = models.CharField(max_length=100, unique=True)
    priority = models.IntegerField()
    created = models.DateTimeField()
    duration = models.DurationField()
    expires = models.DateTimeField()
    todolist = models.ForeignKey('Profile', on_delete=models.CASCADE)
    
    def __unicode__(self):
        return self.name



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

