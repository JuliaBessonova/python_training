from model.contact import Contact
import random

def test_change_first_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", homephone="81111111111", email="test@test.com"))
    old_contacts = db.get_contact_list()
    mcontact = random.choice(old_contacts)
    contact = Contact(id=mcontact.id, firstname="Joseph", lastname="Stalin", address="New York", homephone="82222222222", email="qwe@qwe.com")
    app.contact.change_contact_by_id(mcontact.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts.remove(mcontact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
