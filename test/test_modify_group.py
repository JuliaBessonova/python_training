from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    mgroup = random.choice(old_groups)
    group = Group(id=mgroup.id, name="New group")
    app.group.modify_group_by_id(mgroup.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups.remove(mgroup)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_change_first_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(header="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header=" Changed header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
