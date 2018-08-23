from django.contrib.auth.models import User
from rest_framework import serializers

from . import models

class AddressSerializer(serializers.ModelSerializer):
    """Serializer that maps the Address Model to JSON."""

    class Meta:
        model = models.Address
        fields = ('id', 'title', 'owner')


class PhoneNumberSerializer(serializers.ModelSerializer):
    """Serializer that maps the PhoneNumber Model to JSON."""

    class Meta:
        model = models.PhoneNumber
        fields = ('id', 'number', 'owner')


class EmailSerializer(serializers.ModelSerializer):
    """Serializer that maps the Email Model to JSON."""

    class Meta:
        model = models.Email
        fields = ('id', 'address', 'owner')


class ContactSerializer(serializers.ModelSerializer):
    """Serializer that maps the Contact Model to JSON."""
    addresses = AddressSerializer(many=True, read_only=True)
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)

    class Meta:
        model = models.Contact
        fields = (
            'id',
            'first_name',
            'last_name',
            'date_of_birth',
            'addresses',
            'phone_numbers',
            'emails',
            'avatar',
            'notes',
            'created_at',
        )
        read_only_fields = ('created_at',)
