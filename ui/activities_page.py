from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
)
from PyQt6.QtCore import Qt


class ActivitiesPage(QWidget):
    """Display all available activities in a list."""

    def __init__(self, manager):
        """Initialize the activities page with an activity manager."""
        super().__init__()

        layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        for activity in manager.get_activities():
            item = QListWidgetItem(
                f"{activity.name} - {activity.date}"
            )
            item.setData(Qt.ItemDataRole.UserRole, activity)
            self.list_widget.addItem(item)

        self.list_widget.itemClicked.connect(self.show_details)

    def show_details(self, item):
        """Show a popup with the clicked activity's details."""
        activity = item.data(Qt.ItemDataRole.UserRole)
        QMessageBox.information(self, activity.name, str(activity))
