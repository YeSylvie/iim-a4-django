from django.test import TestCase
from .models import Contact, UploadCvFile
from django.urls import reverse
from .forms import ContactForm, UploadCvFileForm
from http import HTTPStatus


class ContactFormCase(TestCase):
    def setUp(self):
        new_contact = Contact.objects.create(
            lastname='Sysyy',
            firstname='Ye',
            email='sysy@test.com',
            message='Ceci est un test unitaire.'
        )
        new_contact.save()

        new_contact2 = Contact.objects.create(
            lastname='Sysyy2',
            firstname='Ye2',
            email='sysy2@test.com',
            message='Ceci est un test unitaire2.'
        )
        new_contact2.save()   

    def test_all_message(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['messages']) == 2)

    def test_valid_data(self):
        form = ContactForm({
            'lastname': "Turanga",
            'firstname': "Leela",
            'email': "test@gmail.com",
            'message': "Hi there",
        })
        self.assertTrue(form.is_valid())
        contact = form.save()
        self.assertEqual(contact.lastname, "Turanga")
        self.assertEqual(contact.firstname, "Leela")
        self.assertEqual(contact.email, "test@gmail.com")
        self.assertEqual(contact.message, "Hi there")

    def test_new_message_is_registered(self):
        old_length_messages = Contact.objects.count() 
        lastname='newLastName',
        firstname='newFirstName',
        email='nex@test.com',
        message='Ceci est un new message.'
        response = self.client.post(reverse('new-contact'), {
            'firstname': firstname,
            'lastname': lastname,
            'email': email,
            'message': message
        })
        new_lenght_message = Contact.objects.count() 
        self.assertRedirects(response, '/contact')
        self.assertEqual(new_lenght_message, old_length_messages + 1) 

    def test_not_valid_form(self):
        data = {'firstname': "firstname",
            'lastname': "lastname",
            'email': "email@gmail.com"
        }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
        response = self.client.post(reverse('new-contact'), data)
        self.assertEquals(response.status_code, 500)

    def test_valid_form_contact(self):
        data = {'firstname': "firstname",
            'lastname': "lastname",
            'email': "email@gmail.com",
            'message': "Petit message"
        }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())


class ViewTestCase(TestCase):
   
    def test_view_contact_uses_correct_template(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formation/contact.html')

    def test_view_apply_uses_correct_template(self):
        response = self.client.get(reverse('apply'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formation/apply.html')

    def test_view_index_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formation/index.html')
    
    def test_view_dashboard_uses_correct_template(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'formation/dashboard.html')