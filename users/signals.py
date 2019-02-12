'''
We want to create a default profile whenever a a User is created
'''


from django.db.models.signals import post_save #post-save is the signal that gets fired when an object gets saved in db.
from django.contrib.auth.models import User	  #User will be sender

from django.dispatch import receiver
from .models import Profile	


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()