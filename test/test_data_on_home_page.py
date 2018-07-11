import re
from model.contact import Contact

def test_data_on_home_page(app, db):
    uicontacts = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    dbcontacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for contact in range(len(uicontacts)):
        assert uicontacts[contact].lastname == dbcontacts[contact].lastname
        assert uicontacts[contact].firstname == dbcontacts[contact].firstname
        assert uicontacts[contact].address == dbcontacts[contact].address
        assert uicontacts[contact].all_emails_from_home_page == merge_emails_like_on_home_page(dbcontacts[contact])
        assert uicontacts[contact].all_phones_from_home_page == merge_phones_like_on_home_page(dbcontacts[contact])

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))
