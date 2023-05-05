from users.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create superusers"

    def add_arguments(self, parser):
        parser.add_argument(
            "--username",
            default='admin',
            type=str,
            help="Defines username register",
        )
        parser.add_argument(
            "--email",
            default='admin@example.com',
            type=str,
            help="Defines email register",
        )
        parser.add_argument(
            "--password",
            default='admin1234',
            type=str,
            help="Defines password register",
        )

    def handle(self, *args, **kwargs):
        username = kwargs["username"]
        email = kwargs["email"]
        password = kwargs["password"]
        try:
            user = User.objects.create_superuser(
                username=username,
                email=f"{username}@example.com",
                password=password,
            )
        except user.UsernameAlreadyExist:
            CommandError(f'Username {username} already taken.')

        except user.EmailAlreadyExist:
            CommandError(f'Email {email} already taken.')

        self.stdout.write(self.style.SUCCESS(f'Admin {username} successfully created!'))
