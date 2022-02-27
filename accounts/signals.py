from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from accounts.models import Profile
from django.conf import settings
from rest_framework.authtoken.models import Token

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    if created:
        #Profile.objects.create(user=instance)
        Token.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_user_profile(sender, instance, **kwargs):
#     instance.user_profile.save()
