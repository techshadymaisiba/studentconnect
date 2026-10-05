from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QStackedWidget,
)

from services.activity_manager import ActivityManager
from models.my_list import MyList
from ui.activities_page import ActivitiesPage
from ui.search_page import SearchPage
from ui.my_list_page import MyListPage
from ui.home_page import HomePage


class MainWindow(QMainWindow):
    """Main window for the StudentConnect application."""

    def __init__(self):
        """Initialize the StudentConnect main window."""
        super().__init__()
        self.setWindowTitle("StudentConnect")

        self.manager = ActivityManager("data/activities.json")
        self.my_list = MyList()

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)

        # Menu on the left
        menu_layout = QVBoxLayout()

        home_button = QPushButton("Home")
        activities_button = QPushButton("Activities")
        search_button = QPushButton("Search")
        my_list_button = QPushButton("My List")
        exit_button = QPushButton("Exit")

        menu_layout.addWidget(home_button)
        menu_layout.addWidget(activities_button)
        menu_layout.addWidget(search_button)
        menu_layout.addWidget(my_list_button)
        menu_layout.addWidget(exit_button)
        menu_layout.addStretch()

        main_layout.addLayout(menu_layout)

        # Pages on the right
        self.pages = QStackedWidget()

        self.pages.addWidget(HomePage(self.show_activities))
        self.pages.addWidget(ActivitiesPage(self.manager, self.my_list))
        self.pages.addWidget(SearchPage(self.manager))

        self.my_list_page = MyListPage(self.my_list, self.show_home)
        self.pages.addWidget(self.my_list_page)

        main_layout.addWidget(self.pages)

        # Button connections
        home_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(0)
        )

        activities_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(1)
        )

        search_button.clicked.connect(
            lambda: self.pages.setCurrentIndex(2)
        )

        my_list_button.clicked.connect(self.show_my_list)

        exit_button.clicked.connect(self.close)
    def show_home(self):
        """Display the Home page."""
        self.pages.setCurrentIndex(0)

    def show_activities(self):
        """Display the Activities page."""
        self.pages.setCurrentIndex(1)

    def show_my_list(self):
        """Refresh and display the My List page."""
        self.my_list_page.refresh()
        self.pages.setCurrentIndex(3)