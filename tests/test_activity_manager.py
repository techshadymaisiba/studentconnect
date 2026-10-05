import pytest
from services.activity_manager import ActivityManager


def test_load_count():
    manager = ActivityManager("data/activities.json")
    activities = manager.get_activities()
    assert len(activities) == 4


def test_find_activity_by_name_found():
    manager = ActivityManager("data/activities.json")
    activity = manager.find_activity_by_name("Sports Day")
    assert activity is not None
    assert activity.name == "Sports Day"


def test_find_activity_by_name_not_found():
    manager = ActivityManager("data/activities.json")
    activity = manager.find_activity_by_name("Nonexistent Event")
    assert activity is None


def test_search_activities_by_keyword_found():
    manager = ActivityManager("data/activities.json")
    results = manager.search_activities("sports")
    assert len(results) == 1
    assert results[0].name == "Sports Day"
    assert any("sports" in activity.name.lower() for activity in results)

def test_search_activities_empty_keyword():
    manager = ActivityManager("data/activities.json")
    results = manager.search_activities("")
    assert len(results) == 0
    assert results == []  
    
def test_load_missing_file():
    with pytest.raises(FileNotFoundError):
        ActivityManager("data/nonexistent.json")



