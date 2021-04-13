# account
# from django.contrib import auth
from django.contrib.auth.models import User, PermissionsMixin
from django.db import models
from django.utils import timezone
from phone_field import PhoneField
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(User, PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

# pip install django-phone-field
# https://pypi.org/project/django-phone-field/
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional items not defaulted in the Django User
    phone = PhoneField(blank=True, help_text='Contact phone number')
    title = models.CharField(max_length=255)
    system_name = models.ForeignKey('myapp.Agency', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


# class UserProfileInfo(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     #additional items not defaulted in the Django User
#     phone = PhoneField(blank=True, help_text='Contact phone number')
#     title = models.CharField(max_length=255)
#     system_name = models.ForeignKey('myapp.Agency', on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username