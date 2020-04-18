from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from user_profile.models import User
from user_profile.tasks import signal_write_db


# 10. signals - create signal handler, that creates a note in database when every model is created/edited/deleted.
@receiver(post_save)
def model_changed(sender, instance, **kwargs):
    class_name = instance.__class__.__name__
    if class_name not in ['ModelSaveSignal', ]:
        info = f'{class_name} with id {instance.id} modified'
        signal_write_db.delay(info)


@receiver(pre_delete)
def model_deleted(sender, instance, **kwargs):
    class_name = instance.__class__.__name__
    if class_name not in ['ModelSaveSignal', ]:
        info = f'{class_name} with id {instance.id} deleted'
        signal_write_db.delay(info)
