class Activity:
    def __init__(self, name, date, time, location, description):
        self.name = name
        self.date = date
        self.time = time
        self.location = location
        self.description = description

    def __str__(self):
        return (
            f"Activity:\n"
            f"{self.name}\n"
            f"Date: {self.date}\n"
            f"Time: {self.time}\n"
            f"Location: {self.location}\n"
            f"Description: {self.description}"
        )

