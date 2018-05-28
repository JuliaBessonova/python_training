# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", phone="81111111111", email="test@test.com"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="", lastname="", address="", phone="", email=""))
    app.session.logout()
