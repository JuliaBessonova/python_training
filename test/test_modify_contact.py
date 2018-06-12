from model.contact import Contact

def test_change_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", phone="81111111111", email="test@test.com"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Joseph", lastname="Stalin", address="New York", phone="82222222222", email="qwe@qwe.com")
    contact.id = old_contacts[0].id
    app.contact.change_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
