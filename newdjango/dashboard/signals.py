from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Profile
from  django.dispatch import receiver

#@receiver(post_save,sender=User)
def user_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='profile')
		instance.groups.add(group)
		Profile.objects.create(user=instance,username=instance.username,email=instance.email)
		print('Profile created!')

post_save.connect(user_profile, sender=User)

@receiver(post_save,sender=User)
def update_profile(sender, instance, created, **kwargs):

	if created == False:
		instance.profile.save()
		print("profile updated")

#post_save.connect(update_profile, sender=User)
