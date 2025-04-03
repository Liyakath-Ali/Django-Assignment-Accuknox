#Author : Shaik Ali <liyakathliyu2@gmail.com>
#Description: 

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import user
import threading

@receiver(post_save, sender=User)
def signal_handler(sender,instance,**kwargs):
    print(f"Signal received in thread: {threading.current_thread().name}")

#create a new user
user= User.objects.create(username="testuser")

#print current thread
print(f"Main thread: {threading.current_thread().name}")
