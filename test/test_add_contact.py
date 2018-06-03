# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", phone="81111111111", email="test@test.com"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", phone="", email=""))

