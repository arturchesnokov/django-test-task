from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType


# 9. commands - create django command that prints all models and object counts.
class Command(BaseCommand):
    help = 'Prints all models and objects counts'

    def handle(self, *args, **options):
        models = ContentType.objects.all()

        return ''.join(
            f'Model: {model}, objects q-ty: {model.get_all_objects_for_this_type().count()} \n' for model in models)
