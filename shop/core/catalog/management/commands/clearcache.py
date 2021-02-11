from django.core.management.base import BaseCommand
from catalog.models import Thumb
from django.utils import timezone

class Command(BaseCommand):
    help = 'Sync Beles'

    def handle(self, *args, **options):
        time = timezone.now()
        Thumb.objects.all().delete()

        print('Потрачено времени: %s' % (timezone.now() - time))
        print('Завершено.')