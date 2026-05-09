from allauth.account.models import EmailAddress
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError
from django.dispatch import receiver

@receiver(pre_save, sender=EmailAddress)
def check_unique_verified_email(sender, instance, **kwargs):
    if instance.verified:
        exists = EmailAddress.objects.filter(
            email=instance.email,
            verified=True
        ).exclude(pk=instance.pk).exists()
        if exists:
            raise ValidationError("Este e-mail já está verificado para outro usuário.")
