import random
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", homephone="81111111111", email="test@test.com"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    contacts = db.get_contact_list()
    groups = db.get_group_list()
    contact = random.choice(contacts)
    group = random.choice(groups)
    app.contact.add_contact_to_group_by_id(contact_id=contact.id, group_id=group.id)
    contacts_in_group = orm.get_contacts_in_group(group)
    for item in contacts_in_group:
        if item.id == contact.id:
            assert True