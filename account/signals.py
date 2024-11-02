from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.timezone import now
from ecommerce.utils.monday_api import add_user_to_board

@receiver(post_save, sender=User)
def add_user_to_monday_board(sender, instance, created, **kwargs):
    if created:  # Only trigger when a new user is created
        username = instance.username
        email = instance.email
        registration_date = now().strftime('%Y-%m-%d')  # Format the registration date

        # Add user to Monday.com board  
        add_user_to_board(username, email, registration_date)
