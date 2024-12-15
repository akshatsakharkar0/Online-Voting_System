from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from voting.models import Voter

@receiver(post_save, sender=User)
def create_voter(sender, instance, created, **kwargs):
    if created:
        Voter.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_voter(sender, instance, **kwargs):
    if hasattr(instance, 'voter'):
        instance.voter.save()
