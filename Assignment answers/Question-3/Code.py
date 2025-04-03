from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import user

@receiver(post_save, sender=User)
def signal_handler(sender,instance, **kwargs):
    print(f"Signal executed inside transaction: {transaction.get_autocommit()}")

with transaction.atomic():
    user= User.objects.create(username="testuser")
    print(f"Inside transaction block:{transaction.get_autocommit()}")
