
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget

class ActivitiesPage(QWidget):

    def __init__(self, manager):
        super().__init__()

        layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        for activity in manager.get_activities():
            self.list_widget.addItem(
                f"{activity.name} - {activity.date}"
            )