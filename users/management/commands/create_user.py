from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """
    Command to create a user. Only the active user can interact with the API.
    """

    def handle(self, *args, **options):
        email_adress = input("email ")
        f_name = input("first_name ")
        l_name = input("last_name ")
        password = input("password ")

        user = User.objects.create(
            email=email_adress,
            first_name=f_name,
            last_name=l_name,
            is_staff=False,
            is_active=True
        )

        user.set_password(password)
        user.save()
