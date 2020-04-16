from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from user_profile.models import User
from user_profile.tasks import signal_write_db


# 10. signals - create signal handler, that creates a note in database when every model is created/edited/deleted.
@receiver(post_save, sender=User)
def model_changed(sender, instance, **kwargs):
    info = f'user {instance.username} has been modified'
    signal_write_db.delay(info)


@receiver(pre_delete, sender=User)
def model_deleted(sender, instance, **kwargs):
    info = f'user {instance.username} has been deleted'
    signal_write_db.delay(info)
