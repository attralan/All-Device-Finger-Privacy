"""
Fingerprint Laptop Unlock System

Main GUI Window

GUI Layer
|
Application Controller
|
Backend Services

Version:
2.0
"""


from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QStackedWidget,
    QStatusBar
)


from PySide6.QtCore import Qt



from gui.dashboard import DashboardPage
from gui.device_page import DevicePage
from gui.logs_page import LogsPage
from gui.settings import SettingsPage




class MainWindow(QMainWindow):
    """
    Main application window.
    """



    def __init__(
        self,
        controller
    ):

        super().__init__()


        # Store controller

        self.controller = controller



        self.setWindowTitle(
            "Fingerprint Laptop Unlock System"
        )


        self.resize(
            1200,
            700
        )


        self.create_ui()



    def create_ui(self):
        """
        Create complete GUI.
        """

        main_widget = QWidget()


        main_layout = QHBoxLayout()



        # =========================
        # Sidebar
        # =========================


        sidebar = QWidget()


        sidebar_layout = QVBoxLayout()



        title = QLabel(
            "Fingerprint\nUnlock"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet(
            """
            font-size:24px;
            font-weight:bold;
            padding:20px;
            """
        )



        self.start_button = QPushButton(
            "Start Server"
        )


        self.stop_button = QPushButton(
            "Stop Server"
        )



        dashboard_button = QPushButton(
            "Dashboard"
        )


        device_button = QPushButton(
            "Devices"
        )


        logs_button = QPushButton(
            "Logs"
        )


        settings_button = QPushButton(
            "Settings"
        )



        sidebar_layout.addWidget(
            title
        )


        sidebar_layout.addWidget(
            self.start_button
        )


        sidebar_layout.addWidget(
            self.stop_button
        )


        sidebar_layout.addSpacing(
            20
        )


        sidebar_layout.addWidget(
            dashboard_button
        )


        sidebar_layout.addWidget(
            device_button
        )


        sidebar_layout.addWidget(
            logs_button
        )


        sidebar_layout.addWidget(
            settings_button
        )


        sidebar_layout.addStretch()



        sidebar.setLayout(
            sidebar_layout
        )


        sidebar.setFixedWidth(
            220
        )



        # =========================
        # Pages
        # =========================


        self.pages = QStackedWidget()



        self.dashboard_page = DashboardPage(
    self.controller
)


        self.device_page = DevicePage(
    self.controller
)


        self.logs_page = LogsPage(
    self.controller
)


        self.settings_page = SettingsPage()



        self.pages.addWidget(
            self.dashboard_page
        )


        self.pages.addWidget(
            self.device_page
        )


        self.pages.addWidget(
            self.logs_page
        )


        self.pages.addWidget(
            self.settings_page
        )



        # =========================
        # Navigation
        # =========================


        dashboard_button.clicked.connect(

            lambda:
            self.pages.setCurrentWidget(
                self.dashboard_page
            )

        )



        device_button.clicked.connect(

            lambda:
            self.pages.setCurrentWidget(
                self.device_page
            )

        )



        logs_button.clicked.connect(

            lambda:
            self.pages.setCurrentWidget(
                self.logs_page
            )

        )



        settings_button.clicked.connect(

            lambda:
            self.pages.setCurrentWidget(
                self.settings_page
            )

        )



        # =========================
        # Server Controls
        # =========================


        self.start_button.clicked.connect(

            self.start_server

        )



        self.stop_button.clicked.connect(

            self.stop_server

        )



        # =========================
        # Main Layout
        # =========================


        main_layout.addWidget(
            sidebar
        )


        main_layout.addWidget(
            self.pages
        )



        main_widget.setLayout(
            main_layout
        )


        self.setCentralWidget(
            main_widget
        )



        self.setStatusBar(
            QStatusBar()
        )


        self.statusBar().showMessage(
            "System Ready"
        )



    def start_server(self):
        """
        Start backend server.
        """


        try:

            self.controller.start_server()


            self.statusBar().showMessage(
                "Communication Server Running"
            )


        except Exception as error:


            self.statusBar().showMessage(
                f"Start Failed: {error}"
            )



    def stop_server(self):
        """
        Stop backend server.
        """


        try:

            self.controller.stop_server()


            self.statusBar().showMessage(
                "Communication Server Stopped"
            )


        except Exception as error:


            self.statusBar().showMessage(
                f"Stop Failed: {error}"
            )