"""
Fingerprint Laptop Unlock System

Professional Dashboard Page

Features:
- Server status monitoring
- Security overview
- System information

PySide6 GUI

Version:
2.0
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QFrame
)


from PySide6.QtCore import Qt





class StatusCard(QFrame):
    """
    Reusable dashboard information card.
    """



    def __init__(
        self,
        title,
        content
    ):

        super().__init__()


        self.create_ui(
            title,
            content
        )



    def create_ui(
        self,
        title,
        content
    ):

        layout = QVBoxLayout()



        title_label = QLabel(
            title
        )


        title_label.setStyleSheet(
            """
            font-size:18px;
            font-weight:bold;
            """
        )



        self.content_label = QLabel(
            content
        )


        self.content_label.setStyleSheet(
            """
            font-size:15px;
            """
        )


        self.content_label.setWordWrap(
            True
        )



        layout.addWidget(
            title_label
        )


        layout.addWidget(
            self.content_label
        )



        self.setLayout(
            layout
        )



    def update_content(
        self,
        text
    ):

        self.content_label.setText(
            text
        )





class DashboardPage(QWidget):
    """
    Main dashboard.

    Receives updates from ApplicationController.
    """



    def __init__(
        self,
        controller=None
    ):

        super().__init__()


        self.controller = controller



        self.server_card = None


        self.create_ui()



        self.connect_signals()



    def create_ui(self):

        main_layout = QVBoxLayout()



        # =========================
        # Title
        # =========================


        title = QLabel(
            "System Dashboard"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        title.setStyleSheet(
            """
            font-size:30px;
            font-weight:bold;
            """
        )


        main_layout.addWidget(
            title
        )



        # =========================
        # Top Cards
        # =========================


        cards_layout = QHBoxLayout()



        self.server_card = StatusCard(

            "Communication Server",

            """
🔴 OFFLINE

Port: 8080

Status: Stopped

"""

        )



        security_card = StatusCard(

            "Security Status",

            """
🔒 Encryption

     ENABLED


🛡 Replay Protection

     ENABLED


📱 Device Trust

     ENABLED

"""

        )



        cards_layout.addWidget(
            self.server_card
        )


        cards_layout.addWidget(
            security_card
        )



        main_layout.addLayout(
            cards_layout
        )



        # =========================
        # System Information
        # =========================


        system_card = StatusCard(

            "System Information",

            """
Application:

Fingerprint Laptop Unlock System


Version:

1.0


Status:

Ready

"""

        )



        main_layout.addWidget(
            system_card
        )



        main_layout.addStretch()



        self.setLayout(
            main_layout
        )



    def connect_signals(self):
        """
        Connect backend signals.
        """


        if self.controller is None:

            return



        self.controller.signals.server_started.connect(

            self.server_online

        )



        self.controller.signals.server_stopped.connect(

            self.server_offline

        )



    def server_online(self):
        """
        Update dashboard when server starts.
        """


        self.server_card.update_content(

            """
🟢 ONLINE

Port: 8080

Status: Running

"""

        )



    def server_offline(self):
        """
        Update dashboard when server stops.
        """


        self.server_card.update_content(

            """
🔴 OFFLINE

Port: 8080

Status: Stopped

"""

        )