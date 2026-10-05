from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QMessageBox,
)
from PyQt6.QtCore import Qt


class MyListPage(QWidget):
    """Display activities saved by the user."""

    def __init__(self, my_list):
        """Initialize the My List page with the saved activities."""
        super().__init__()

        self.my_list = my_list

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("MY ACTIVITIES"))

        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        buttons = QHBoxLayout()

        remove_button = QPushButton("Remove")
        back_button = QPushButton("Back")

        buttons.addWidget(remove_button)
        buttons.addWidget(back_button)

        layout.addLayout(buttons)

        remove_button.clicked.connect(self.remove_selected)

        self.refresh()

    def refresh(self):
        """Refresh the list to show the currently saved activities."""
        self.list_widget.clear()

        for activity in self.my_list.get_items():
            item = QListWidgetItem(
                f"{activity.name} - {activity.date}"
            )
            item.setData(Qt.ItemDataRole.UserRole, activity)
            self.list_widget.addItem(item)

    def remove_selected(self):
        """Remove the selected activity from My List."""
        item = self.list_widget.currentItem()

        if item is None:
            QMessageBox.information(
                self,
                "Remove",
                "Please select an activity first"
            )
            return

        activity = item.data(Qt.ItemDataRole.UserRole)

        self.my_list.remove_item(activity)
        self.refresh()
