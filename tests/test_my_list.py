from models.activity import Activity
from models.my_list import MyList

def make_activity(name, date, time, location, description):
    return Activity(name=name, date=date, time=time, location=location, description=description)


def test_add_item_success():
    my_list = MyList()
    activity = make_activity("Sports Day", "23 September", "10:30 AM", "Sports Grounds", "Join us for a fun-filled day of sports and activities!")
    result = my_list.add_item(activity)
    assert result is True
    assert activity in my_list.get_items()