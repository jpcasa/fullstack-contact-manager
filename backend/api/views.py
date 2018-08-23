from rest_framework import generics, permissions
from django.contrib.auth.models import User
from django.shortcuts import render

from . import serializers
from .permissions import (IsOwnerContact,
                          IsOwnerAddress,
                          isOwnerPhoneNumber, isOwnerEmail)
from . import models


class AddressView(generics.ListCreateAPIView):
    """Handles GET and POST requests for the Address Model."""
    serializer_class = serializers.AddressSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerAddress,)

    def get_queryset(self):
        return models.Address.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.owner = self.request.user
        serializer.save()
        last_address = models.Address.objects.latest('id')
        contact_id = self.request.data.get('contact_id', None)
        contact = models.Contact.objects.get(id=contact_id)
        contact.addresses.add(last_address)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
     """Handles GET, PUT, and DELETE requests for the Address Model."""
     queryset = models.Address.objects.all()
     serializer_class = serializers.AddressSerializer
     permission_classes = (permissions.IsAuthenticated, IsOwnerAddress,)


class PhoneNumberView(generics.ListCreateAPIView):
    """Handles GET and POST requests for the PhoneNumber Model."""
    serializer_class = serializers.PhoneNumberSerializer
    permission_classes = (permissions.IsAuthenticated, isOwnerPhoneNumber,)

    def get_queryset(self):
        return models.PhoneNumber.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        last_phone = models.PhoneNumber.objects.latest('id')
        contact_id = self.request.data.get('contact_id', None)
        contact = models.Contact.objects.get(id=contact_id)
        contact.phone_numbers.add(last_phone)


class PhoneNumberDetailView(generics.RetrieveUpdateDestroyAPIView):
     """Handles GET, PUT, and DELETE requests for the PhoneNumber Model."""
     queryset = models.PhoneNumber.objects.all()
     serializer_class = serializers.PhoneNumberSerializer
     permission_classes = (permissions.IsAuthenticated, isOwnerPhoneNumber,)


class EmailView(generics.ListCreateAPIView):
    """Handles GET and POST requests for the Email Model."""
    serializer_class = serializers.EmailSerializer
    permission_classes = (permissions.IsAuthenticated, isOwnerEmail,)

    def get_queryset(self):
        return models.Email.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        last_email = models.Email.objects.latest('id')
        contact_id = self.request.data.get('contact_id', None)
        contact = models.Contact.objects.get(id=contact_id)
        contact.emails.add(last_email)


class EmailDetailView(generics.RetrieveUpdateDestroyAPIView):
     """Handles GET, PUT, and DELETE requests for the Email Model."""
     queryset = models.Email.objects.all()
     serializer_class = serializers.EmailSerializer
     permission_classes = (permissions.IsAuthenticated, isOwnerEmail,)


class CreateView(generics.ListCreateAPIView):
    """Handles GET and POST requests for the Contact Model."""
    # queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerContact,)

    def get_queryset(self):
        return models.Contact.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """Handles GET, PUT, and DELETE requests for the Contact Model."""
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerContact,)
