# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="", email="",
                    email2="", email3="", secondaryphone="")] + [
    Contact(firstname=random_string("firstnamename", 10), lastname=random_string("lastname", 10), address=random_string("address", 20),
            homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
            email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), secondaryphone=random_string("secondaryphone", 10))
    for i in range(2)
]

@pytest.mark.parametrize("contact", testdata, ids=[str(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



