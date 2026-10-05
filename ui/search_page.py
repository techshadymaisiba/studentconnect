from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QPushButton,
    QListWidget,
    QLabel,
    QMessageBox,
)


class SearchPage(QWidget):
    """Allow users to search for activities by keyword."""

    def __init__(self, manager):
        """Initialize the search page with an activity manager."""
        super().__init__()

        self.manager = manager

        layout = QVBoxLayout(self)

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("Search activities...")
        layout.addWidget(self.search_box)

        search_button = QPushButton("Search")
        layout.addWidget(search_button)

        self.message_label = QLabel("")
        layout.addWidget(self.message_label)

        self.results = QListWidget()
        layout.addWidget(self.results)

        search_button.clicked.connect(self.run_search)

    def run_search(self):
        """Display activities that match the search keyword."""
        self.results.clear()
        self.message_label.setText("")

        keyword = self.search_box.text().strip()

        if not keyword:
            self.message_label.setText("Please type a keyword")
            return

        found = self.manager.search_activities(keyword)

        if not found:
            self.message_label.setText("No activities found")
            return

        for activity in found:
            self.results.addItem(
                f"{activity.name} - {activity.date}"
            )
