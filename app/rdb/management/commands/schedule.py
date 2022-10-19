from django.core.management.base import BaseCommand, CommandError
from django_q.tasks import async_task, schedule
from django_q.models import Schedule


class Command(BaseCommand):
    help = "Schedules imports to database"
    def handle(self, *args, **options):
        try:
            print('Command is executed')
            schedule("rdb.tasks.fetch_json", hook="rdb.tasks.validate_and_save", schedule_type=Schedule.WEEKLY)
        except Exception as e:
            raise CommandError(e)