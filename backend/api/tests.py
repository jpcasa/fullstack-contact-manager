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


class ViewTestCase(TestCase):
    """Test Class for api views."""

    def setUp(self):
        """Define the test client."""
        self.user = User.objects.create(username="jpcasa")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.contact_data = {'first_name': 'Juan', 'last_name': 'Casabianca'}
        self.response = self.client.post(
            reverse('create'),
            self.contact_data,
            format='json',
        )

        self.response_address = self.client.post(
            reverse('addresses'),
            {'title': 'Times Square, NY'},
            format='json',
        )

        self.response_phone = self.client.post(
            reverse('phones'),
            {'number': '3507015800'},
            format='json',
        )

        self.response_email = self.client.post(
            reverse('emails'),
            {'address': 'hello@email.com'},
            format='json',
        )


    def test_authorization_enforced(self):
        """Test API for User Auth"""
        new_client = APIClient()
        response = new_client.get('/contacts/', kwargs={'pk': 1}, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_api_can_create_contact(self):
        """Test API for contact creation."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)


    def test_api_can_crud_address(self):
        """Test CRUD functionality for Address Model."""
        # Tests Creation
        self.assertEqual(
            self.response_address.status_code,
            status.HTTP_201_CREATED
        )

        # Tests Update
        address = models.Address.objects.get()
        new_address = 'Liberty Square'
        response = self.client.put(
            reverse('address_detail', kwargs={'pk': address.id}),
            {'title': new_address},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, new_address)

        # Test Delete
        response = self.client.delete(
            reverse('address_detail', kwargs={'pk': address.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_api_can_crud_phones(self):
        """Test CRUD functionality for Phone Model."""
        # Tests Creation
        self.assertEqual(
            self.response_phone.status_code,
            status.HTTP_201_CREATED
        )

        # Tests Update
        phone = models.PhoneNumber.objects.get()
        new_phone = '+(1)888-986-587452'
        response = self.client.put(
            reverse('phone_detail', kwargs={'pk': phone.id}),
            {'number': new_phone},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, new_phone)

        # Test Delete
        response = self.client.delete(
            reverse('phone_detail', kwargs={'pk': phone.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_api_can_crud_emails(self):
        """Test CRUD functionality for Email Model."""
        # Tests Creation
        self.assertEqual(
            self.response_email.status_code,
            status.HTTP_201_CREATED
        )

        # Tests Update
        email = models.Email.objects.get()
        new_email = 'hello@othermail.com'
        response = self.client.put(
            reverse('email_detail', kwargs={'pk': email.id}),
            {'address': new_email},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, new_email)

        # Test Delete
        response = self.client.delete(
            reverse('email_detail', kwargs={'pk': email.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_api_can_get_contact(self):
        """Test API to get a contact"""
        contact = models.Contact.objects.get(id=1)
        response = self.client.get(
            '/contacts/',
            kwargs={'pk': contact.id},
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, contact.first_name)


    def test_api_can_update_contact(self):
        """Test API to update a contact"""
        contact = models.Contact.objects.get()
        new_name = 'Rafael'
        change_contact = {'first_name': new_name, 'last_name': 'Gomez'}
        response = self.client.put(
            reverse('details', kwargs={'pk': contact.id}),
            change_contact,
            format='json',
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, new_name)


    def test_api_can_delete_contact(self):
        """Test API to delete a contact"""
        contact = models.Contact.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': contact.id}),
            format='json',
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
