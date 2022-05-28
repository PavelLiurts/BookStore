from django.db import models
from django.contrib.auth.models import Users
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        related_name='profile',
        on_delete=models.CASCADE
    )
    location = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender = User)
def profile_for_new_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance).save()

