from model.contact import Contact

def test_change_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov", address="address", phone="81111111111", email="test@test.com"))
    app.contact.change(Contact(firstname="Joseph", lastname="Stalin", address="New York", phone="82222222222", email="qwe@qwe.com"))
