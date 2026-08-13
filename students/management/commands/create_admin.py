from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create or reset SMT user'

    def handle(self, *args, **kwargs):

        username = 'SMT'
        password = 'smt123'

        user, created = User.objects.get_or_create(
            username=username
        )

        user.set_password(password)
        user.save()

        if created:
            self.stdout.write(
                self.style.SUCCESS(
                    f'User "{username}" created successfully!'
                )
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(
                    f'Password for "{username}" reset successfully!'
                )
            )