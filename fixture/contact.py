from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # create new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("phone2", contact.secondaryphone)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_first_contact(self):
        self.change_contact_by_index(0)

    def change_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        self.open_edit_form_by_index(index)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def change_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        self.open_edit_form_by_id(id)
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def open_edit_form_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a/img")[index].click()

    def open_edit_form_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr/td[8]/a[@href='edit.php?id=%s']/img" % id).click()

    def view_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr/td[7]/a/img")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # approve deletion
        wd.switch_to_alert().accept()
        # go back to home page
        self.go_to_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete']").click()
        # approve deletion
        wd.switch_to_alert().accept()
        # go back to home page
        self.go_to_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def go_to_home_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = element.find_element_by_xpath(".//td[2]").text
                firstname = element.find_element_by_xpath(".//td[3]").text
                address = element.find_element_by_xpath(".//td[4]").text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_edit_form_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, address=address, id=id,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone,
                       email=email, email2=email2, email3=email3)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.view_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone)

    def add_contact_to_group_by_id(self, group_id, contact_id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(contact_id)
        self.choose_group_in_list(group_id)
        wd.find_element_by_name("add").click()
        self.go_to_home_page()

    def choose_group_in_list(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='to_group']/option[@value='%s']" % id).click()

    def remove_contact_from_group_by_id(self, group_id, contact_id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_group_by_id(group_id)
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        self.go_to_home_page()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='group']/option[@value='%s']" % id).click()





