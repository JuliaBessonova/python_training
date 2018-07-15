import random
from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture

orm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", homephone="81111111111", email="test@test.com"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    contacts_in_group = orm.get_contacts_in_group(group)
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    if len(contacts_in_group) == 0:
        app.contact.add_contact_to_group_by_id(contact_id=contact.id, group_id=group.id)
    else:
        contact_in_group = random.choice(contacts_in_group)
        app.contact.remove_contact_from_group_by_id(contact_id=contact_in_group.id, group_id=group.id)
        contacts_not_in_group = orm.get_contacts_not_in_group(group)
        for item in contacts_not_in_group:
            if item.id == contact_in_group.id:
                assert True
