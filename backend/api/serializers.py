from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class AddressSerializer(serializers.ModelSerializer):
    """Serializer that maps the Address Instance to JSON."""

    class Meta:
        model = models.Address
        fields = ('id', 'title')


class PhoneNumberSerializer(serializers.ModelSerializer):
    """Serializer that maps the PhoneNumber Instance to JSON."""

    class Meta:
        model = models.PhoneNumber
        fields = ('id', 'number')


class EmailSerializer(serializers.ModelSerializer):
    """Serializer that maps the Email Instance to JSON."""

    class Meta:
        model = models.Email
        fields = ('id', 'address')


class ContactSerializer(serializers.ModelSerializer):
    """Serializer that maps the Contact Instance to JSON."""

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
            'created_at',
        )
        read_only_fields = ('created_at',)
