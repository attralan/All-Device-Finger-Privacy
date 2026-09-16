"""
Fingerprint Laptop Unlock System

Live Logs Page

PySide6 GUI

Version:
2.0
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)




class LogsPage(QWidget):
    """
    Displays backend logs.
    """



    def __init__(
        self,
        controller=None
    ):

        super().__init__()


        self.controller = controller


        self.create_ui()


        self.connect_signals()



    def create_ui(self):


        layout = QVBoxLayout()



        title = QLabel(
            "System Logs"
        )


        title.setStyleSheet(
            """
            font-size:24px;
            font-weight:bold;
            """
        )



        self.logs_view = QTextEdit()


        self.logs_view.setReadOnly(
            True
        )



        clear_button = QPushButton(
            "Clear Logs"
        )



        clear_button.clicked.connect(

            self.clear_logs

        )



        layout.addWidget(
            title
        )


        layout.addWidget(
            self.logs_view
        )


        layout.addWidget(
            clear_button
        )



        self.setLayout(
            layout
        )



    def connect_signals(self):


        if self.controller is None:

            return



        self.controller.log_manager.log_received.connect(

            self.add_log

        )



    def add_log(
        self,
        message
    ):

        self.logs_view.append(

            message

        )



    def clear_logs(self):

        self.logs_view.clear()