from model.contact import Contact

def test_change_first_contact(app):
    app.contact.change(Contact(firstname="Joseph", lastname="Stalin", address="New York", phone="82222222222", email="qwe@qwe.com"))
