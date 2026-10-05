import json
from pathlib import Path

from models.activity import Activity


class ActivityManager:
    """Manage loading, retrieving, and searching activities."""

    def __init__(self, file_path):
        
        self.file_path = Path(file_path)
        self.activities = self.load_activities()

    def load_activities(self):
        
        if not self.file_path.exists():
            raise FileNotFoundError(f"The file {self.file_path} does not exist.")

        with open(self.file_path, 'r', encoding="utf-8") as file:
            data = json.load(file)
            return [Activity(**activity) for activity in data]

    def find_activity_by_name(self, name):
        
        for activity in self.activities:
            if activity.name == name:
                return activity
        return None

    def get_activities(self):
        
        return self.activities

    def search_activities(self, keyword):
        
        keyword_lower = keyword.strip().lower()

        if not keyword_lower:
            return []

        results = []
        for activity in self.activities:
            if (keyword_lower in activity.name.lower() or
                keyword_lower in activity.date.lower() or
                keyword_lower in activity.time.lower() or
                keyword_lower in activity.location.lower() or
                keyword_lower in activity.description.lower()):
                results.append(activity)

        return results

