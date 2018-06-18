

def test_emails_on_home_page(app):
    email_from_home_page = app.contact.get_contact_list()[0]
    email_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert email_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(email_from_edit_page)

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))
