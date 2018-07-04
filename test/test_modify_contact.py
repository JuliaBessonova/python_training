from model.contact import Contact
import random

def test_change_first_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", homephone="81111111111", email="test@test.com"))
    old_contacts = db.get_contact_list()
    mcontact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    contact = Contact(firstname="Joseph", lastname="Stalin", address="New York", homephone="82222222222", email="qwe@qwe.com")
    #contact.id = old_contacts[index].id
    app.contact.change_contact_by_id(mcontat.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    new_contacts = db.get_contact_list()
    #old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
