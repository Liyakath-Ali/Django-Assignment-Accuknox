import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import user

@receiver(post_save, sender=user)
def signal_handler(sender, instance, **kwargs):
    print(f"Signal executed in the thread:{threading.current().name}")
    
print(f"Main thread before saving user:{threading.cuurent_thread().name}")
user= User.objects.create(username="testuser")
print(f"Main thread after saving user:{threading.current_thread().name}")
