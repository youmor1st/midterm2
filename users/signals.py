from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.utils.timezone import now
from django.contrib.auth.models import User
import logging

user_logger = logging.getLogger('user_actions')

@receiver(post_save, sender=User)
def log_user_registration(sender, instance, created, **kwargs):
    if created:
        user_logger.info(f"User registered: {instance.username} at {now()}")

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    user_logger.info(f"User logged in: {user.username} at {now()}")

@receiver(user_logged_out)
def log_user_logout(sender, request, user, **kwargs):
    user_logger.info(f"User logged out: {user.username} at {now()}")
