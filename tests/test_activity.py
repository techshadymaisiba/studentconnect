from models.activity import Activity


def test_activity_creation():
    activity = Activity(
        name="Sports Day",
        date="23 September",
        time="10:30 AM",
        location="Sports Grounds",
        description="Join us for a fun-filled day of sports and activities!"
    )
    assert activity.name == "Sports Day"
    assert activity.date == "23 September"
    assert activity.time == "10:30 AM"
    assert activity.location == "Sports Grounds"
    assert activity.description == "Join us for a fun-filled day of sports and activities!"


def test_activity_str():
    activity = Activity(
        name="Sports Day",
        date="23 September",
        time="10:30 AM",
        location="Sports Grounds",
        description="Join us for a fun-filled day of sports and activities!"
    )
    expected_str = (
        "Activity:\n"
        "Sports Day\n"
        "Date: 23 September\n"
        "Time: 10:30 AM\n"
        "Location: Sports Grounds\n"
        "Description: Join us for a fun-filled day of sports and activities!"
    )
    assert str(activity) == expected_str