from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse

from . import models

class ModelsTestCase(TestCase):
    """Test Class for the Models."""

    def setUp(self):
        """Define the test client."""
        self.user = User.objects.create(username="jpcasa")

        self.address_title = "Calle 92 #13-68"
        self.phone_number = "+(57) 350-701-5800"
        self.email_address = "hola@jpcasabianca.com"

        self.address = models.Address(
            title=self.address_title
        )
        self.phone = models.PhoneNumber(
            number=self.phone_number
        )
        self.email = models.Email(
            address=self.email_address
        )

        self.first_name = "Juan"
        self.last_name = "Casabianca"
        self.contact = models.Contact(
            owner=self.user,
            first_name=self.first_name,
            last_name=self.last_name
        )

    def test_model_can_create_address(self):
        """Test the address model creation."""
        old = models.Address.objects.count()
        self.address.save()
        new = models.Address.objects.count()
        self.assertNotEqual(old, new)


    def test_model_can_create_phone(self):
        """Test the phone number model creation."""
        old = models.PhoneNumber.objects.count()
        self.phone.save()
        new = models.PhoneNumber.objects.count()
        self.assertNotEqual(old, new)


    def test_model_can_create_email(self):
        """Test the email model creation."""
        old = models.Email.objects.count()
        self.email.save()
        new = models.Email.objects.count()
        self.assertNotEqual(old, new)


    def test_model_can_create_contact(self):
        """Test the contact model creation."""
        old = models.Contact.objects.count()
        self.contact.save()
        new = models.Contact.objects.count()
        self.assertNotEqual(old, new)


    def test_model_creates_succesfully(self):
        """Test that contact creates with correct values"""
        self.contact.save()
        new_contact = models.Contact.objects.latest('id')
        self.assertEqual(new_contact.first_name, self.first_name)


    def test_model_can_update_user(self):
        """Test that a contact updates successfully"""
        new_first_name = "Alfredo"
        self.contact.save()
        self.assertNotEqual(new_first_name, self.contact.first_name)
        self.contact.first_name = new_first_name
        self.contact.save()
        self.assertEqual(new_first_name, self.contact.first_name)


    def test_model_can_update_address(self):
        """Test that an address updates successfully"""
        new_address = "Times Square"
        self.address.save()
        self.assertNotEqual(new_address, self.address.title)
        self.address.title = new_address
        self.address.save()
        self.assertEqual(new_address, self.address.title)



    def test_model_can_update_email(self):
        """Test that an email updates successfully"""
        new_address = "hi@email.com"
        self.email.save()
        self.assertNotEqual(new_address, self.email.address)
        self.email.address = new_address
        self.email.save()
        self.assertEqual(new_address, self.email.address)



    def test_model_can_update_phone(self):
        """Test that a phone updates successfully"""
        new_phone = "Alfredo"
        self.phone.save()
        self.assertNotEqual(new_phone, self.phone.number)
        self.phone.number = new_phone
        self.phone.save()
        self.assertEqual(new_phone, self.phone.number)
