from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtCore import Qt


class ActivitiesPage(QWidget):
    """Display available activities and allow users to save them."""

    def __init__(self, manager, my_list):
        """Initialize the activities page with the manager and saved list."""
        super().__init__()

        self.my_list = my_list

        layout = QVBoxLayout(self)

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        add_button = QPushButton("Add to My List")
        layout.addWidget(add_button)
        add_button.clicked.connect(self.add_selected)

        for activity in manager.get_activities():
            item = QListWidgetItem(
                f"{activity.name} - {activity.date}"
            )
            item.setData(Qt.ItemDataRole.UserRole, activity)
            self.list_widget.addItem(item)

        self.list_widget.itemClicked.connect(self.show_details)

    def show_details(self, item):
        """Show a popup with the selected activity's details."""
        activity = item.data(Qt.ItemDataRole.UserRole)
        QMessageBox.information(
            self,
            activity.name,
            str(activity)
        )

    def add_selected(self):
        """Add the selected activity to My List."""
        item = self.list_widget.currentItem()

        if item is None:
            QMessageBox.information(
                self,
                "Add to My List",
                "Please select an activity first"
            )
            return

        activity = item.data(Qt.ItemDataRole.UserRole)

        added = self.my_list.add_item(activity)

        if added:
            QMessageBox.information(
                self,
                "Added",
                "Activity added to your list"
            )
        else:
            QMessageBox.information(
                self,
                "Already in List",
                "Already in your list"
            )