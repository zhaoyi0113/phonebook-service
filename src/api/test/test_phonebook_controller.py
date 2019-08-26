# coding: utf-8

from __future__ import absolute_import
import unittest
import logging
from flask import json
from six import BytesIO

from api.models.db_contact import DBContact  # noqa: E501
from api.test import BaseTestCase


class TestPhonebookController(BaseTestCase):
    """PhonebookController integration test stubs"""

    def test_add_contact(self):
        """Test case for add_contact

        Add a new contact
        """
        body = {
  "first_name" : "first_name",
  "last_name" : "last_name",
  "password" : "password",
  "userStatus" : 6,
  "phone" : "phone",
  "id" : 0,
  "email" : "email",
  "username" : "username"
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/contact',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        TestPhonebookController.contact_id = response.data.decode('utf-8')
        logging.getLogger('tests').info('contact id = '+ self.contact_id)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_get_contact_by_id(self):
        """Test case for get_contact_by_id

        Find contact by ID
        """
        headers = { 
            'Accept': 'application/json',
            'api_key': 'special-key',
        }
        response = self.client.open(
            '/v2/contact/{contact_id}'.format(contact_id=TestPhonebookController.contact_id),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
                       
    def test_delete_contact(self):
        """Test case for delete_contact

        Deletes a contact
        """
        headers = { 
            'api_key': 'api_key_example',
            'Authorization': 'Bearer special-key',
        }
        logging.getLogger('tests').info('delete contact id ' + TestPhonebookController.contact_id)
        response = self.client.open(
            '/v2/contact/{contact_id}'.format(contact_id=TestPhonebookController.contact_id),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_contacts_by_email(self):
        """Test case for find_contacts_by_email

        Finds contact by email
        """
        query_string = [('email', 'email_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/contact/findByEmail',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_contacts_by_name(self):
        """Test case for find_contacts_by_name

        Finds Contact by name
        """
        query_string = [('name', 'name_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/contact/findByName',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    # @unittest.skip("application/x-www-form-urlencoded not supported by Connexion")
    # def test_update_contact_with_form(self):
    #     """Test case for update_contact_with_form

    #     Updates a contact in phonebook
    #     """
    #     headers = { 
    #         'Content-Type': 'application/x-www-form-urlencoded',
    #         'Authorization': 'Bearer special-key',
    #     }
    #     data = dict(id=56,
    #                 username='username_example',
    #                 first_name='first_name_example',
    #                 last_name='last_name_example',
    #                 email='email_example',
    #                 password='password_example',
    #                 phone='phone_example',
    #                 user_status=56)
    #     response = self.client.open(
    #         '/v2/contact/{contact_id}'.format(contact_id='contact_id_example'),
    #         method='PUT',
    #         headers=headers,
    #         data=data,
    #         content_type='application/x-www-form-urlencoded')
    #     self.assert200(response,
    #                    'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
