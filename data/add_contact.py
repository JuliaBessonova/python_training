from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="name1", lastname="lastname1", address="address", mobilephone="81111111111", workphone="82222222222",
            email="test1@test.com", email2="test2@test.com", email3="test3@test.com", secondaryphone="83333333333")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", homephone="", mobilephone="", workphone="", email="",
                    email2="", email3="", secondaryphone="")] + [
    Contact(firstname=random_string("firstnamename", 10), lastname=random_string("lastname", 10), address=random_string("address", 20),
            homephone=random_string("homephone", 10), mobilephone=random_string("mobilephone", 10), workphone=random_string("workphone", 10),
            email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), secondaryphone=random_string("secondaryphone", 10))
    for i in range(2)
]
