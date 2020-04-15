from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from user_profile.models import User


@receiver(post_save, sender=User)
def model_changed(sender, **kwargs):
    print('model_changed')
