from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
class HomePage(QWidget):
    """Welcome screen of the StudentConnect application."""

    def __init__(self, on_view_activities):
        """Initialize the home page with a callback for viewing activities."""
        super().__init__()

        layout = QVBoxLayout(self)

        layout.addWidget(QLabel("WELCOME"))
        layout.addWidget(QLabel("Welcome to StudentConnect"))

        view_button = QPushButton("View Activities")
        layout.addWidget(view_button)

        view_button.clicked.connect(on_view_activities)