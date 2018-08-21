from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils import timezone
from django.db import models


class Address(models.Model):
    title = models.CharField(max_length=100, default='')
    owner = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=100, default='')
    owner = models.ForeignKey(
        'auth.User',
        related_name='phones',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.number

    class Meta:
        ordering = ('number',)


class Email(models.Model):
    address = models.CharField(max_length=100, default='')
    owner = models.ForeignKey(
        'auth.User',
        related_name='emails',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.address

    class Meta:
        ordering = ('address',)


class Contact(models.Model):
    """This class represents the Contact Model."""
    owner = models.ForeignKey(
        'auth.User',
        related_name='contacts',
        on_delete=models.CASCADE,
        null=True
    )
    first_name = models.CharField(
        blank=False,
        max_length=255,
        default=''
    )
    last_name = models.CharField(
        blank=False,
        max_length=255,
        default=''
    )
    date_of_birth = models.DateTimeField(blank=False, default=timezone.now)
    addresses = models.ManyToManyField(Address, blank=True)
    phone_numbers = models.ManyToManyField(PhoneNumber, blank=True)
    emails = models.ManyToManyField(Email, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        """Readable format for the Model Instance."""
        return '{} {}'.format(self.first_name, self.last_name)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Handles token creation immediately a new user is created."""
    if created:
        Token.objects.create(user=instance)
