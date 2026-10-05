
from PyQt6.QtWidgets import (
 QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QStackedWidget, QLabel,
)

from services.activity_manager import ActivityManager
from ui.activities_page import ActivitiesPage
from ui.search_page import SearchPage
from models.my_list import MyList


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StudentConnect")
        self.resize(800, 600)

        central = QWidget()
        self.setCentralWidget(central)
      
        main_layout = QHBoxLayout(central)

        menu_layout = QVBoxLayout()

        home_button = QPushButton("Home")
        search_button = QPushButton("Search")
        activities_button = QPushButton("Activities")
        my_list_button = QPushButton("My List")
        exit_button = QPushButton("Exit")

        menu_layout.addWidget(home_button)
        menu_layout.addWidget(search_button)
        menu_layout.addWidget(activities_button)
        menu_layout.addWidget(my_list_button)
        menu_layout.addWidget(exit_button)
        menu_layout.addStretch()


        main_layout.addLayout(menu_layout)

        self.manager = ActivityManager("data/activities.json")
        self.my_list = MyList()

        self.pages = QStackedWidget()

        self.pages.addWidget(QLabel("Home Page"))
        self.pages.addWidget(SearchPage(self.manager))
        self.pages.addWidget(ActivitiesPage(self.manager, self.my_list))
        self.pages.addWidget(QLabel("My List Page"))

        main_layout.addWidget(self.pages)

        home_button.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        search_button.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        activities_button.clicked.connect(lambda: self.pages.setCurrentIndex(2))
        my_list_button.clicked.connect(lambda: self.pages.setCurrentIndex(3))
        exit_button.clicked.connect(self.close)



        


        

