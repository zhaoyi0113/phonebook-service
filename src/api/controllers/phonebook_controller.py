import connexion
import six
import json

from api import util
from api.models.db_contact import DBContact
from api.models.db import Session
from flask import abort

def add_contact(body):  # noqa: E501
    """Add a new contact

     # noqa: E501

    :param body: Contact object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        try:
            session = Session()
            body = connexion.request.get_json()
            contact = DBContact(body['username'], body['first_name'], body['last_name'], body['email'], body['password'], body['phone'])
            session.add(contact)
            session.commit()
            session.refresh(contact)
            return json.loads(json.dumps({"id": contact.id}))
        except Exception as error:
            print('save to database failed')
            print(error)
        finally:
            session.close()
    return abort(400, 'something wrong!')


def delete_contact(contact_id, api_key=None):  # noqa: E501
    """Deletes a contact

     # noqa: E501

    :param contact_id: Contact id to delete
    :type contact_id: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    print('delete contact ', contact_id)
    session = Session()
    try:
        query = session.query(DBContact).filter(DBContact.id == contact_id)
        if query.count() == 0:
            return abort(404, 'Not find record')
        contact = query.one()
        session.delete(contact)
        session.commit()
        return 'success'
    except Exception as error:
        print(error)
        return abort(error)
    finally:
        session.close()
    return abort(400, 'failed to delete contact ' + contact_id)


def find_contacts_by_email(email):  # noqa: E501
    """Finds contact by email

    find contact by email address. # noqa: E501

    :param email: Email to filter by
    :type email: str

    :rtype: List[Contact]
    """
    session = Session()
    try:
        contacts = session.query(DBContact).filter(DBContact.email == email).all()
        return util.alchemy_to_json(contacts)
    except Exception as error:
        print(error)
    finally:
        session.close()
    return abort(400, "failed to find contact by email " + email)


def find_contacts_by_name(name):  # noqa: E501
    """Finds Contact by name

    find contact by name # noqa: E501

    :param name: Contact name that need to be considered for filter
    :type name: str

    :rtype: List[Contact]
    """
    session = Session()
    try:
        contacts = session.query(DBContact).filter(DBContact.username == name).all()
        return util.alchemy_to_json(contacts)
    except Exception as error:
        print(error)
    finally:
        session.close()
    return abort(400, "failed to find contact by name" + name)


def get_contact_by_id(contact_id):  # noqa: E501
    """Find contact by ID

    Returns a single contact # noqa: E501

    :param contact_id: ID of contact to return
    :type contact_id: str

    :rtype: Contact
    """
    session = Session()
    try:
        query = session.query(DBContact).filter(DBContact.id == contact_id)
        contact = query.one()
        return util.alchemy_to_json(contact)
    except Exception as error:
        print(error)
        return abort(error)
    finally:
        session.close()
    return abort(400, "failed to find contact by id " + contact_id)

def update_contact_with_form(contact_id, body):
    """Updates a contact in phonebook

     # noqa: E501

    :param contact_id: ID of contact that needs to be updated
    :type contact_id: str
    :param id: 
    :type id: int
    :param username: 
    :type username: str
    :param first_name: 
    :type first_name: str
    :param last_name: 
    :type last_name: str
    :param email: 
    :type email: str
    :param password: 
    :type password: str
    :param phone: 
    :type phone: str
    :param user_status: User Status
    :type user_status: int

    :rtype: None
    """
    session = Session()
    try:
        query = session.query(DBContact).filter(DBContact.id == contact_id)
        if query.count() == 0:
            return abort(404, 'Cannot find contact')
        contact = query.one()
        body = connexion.request.get_json()
        for k, v in body.items():
            if v is not None:
                contact.__setattr__(k, v)
        session.commit()
        return util.alchemy_to_json(contact)
    except Exception as error:
        print(error)
        return abort(error)
    finally:
        session.close()
    return abort(400, 'failed to update')
