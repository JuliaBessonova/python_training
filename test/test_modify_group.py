from model.group import Group

def test_change_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change(Group(name="Changed group", header=" Changed header", footer=" Changed footer"))
    app.session.logout()