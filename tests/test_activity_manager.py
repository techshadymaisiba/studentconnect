from services.activity_manager import ActivityManager


def test_load_count():
    manager = ActivityManager("data/activities.json")
    activities = manager.get_activities()
    assert len(activities) == 4