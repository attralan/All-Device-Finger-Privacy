"""
Application Settings Page
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton
)



class SettingsPage(QWidget):


    def __init__(self):

        super().__init__()

        self.create_ui()



    def create_ui(self):


        layout = QVBoxLayout()



        title = QLabel(
            "Settings"
        )


        host_label = QLabel(
            "Server Host"
        )


        self.host_input = QLineEdit(
            "0.0.0.0"
        )



        port_label = QLabel(
            "Server Port"
        )


        self.port_input = QLineEdit(
            "8080"
        )



        save_button = QPushButton(
            "Save Settings"
        )



        layout.addWidget(
            title
        )

        layout.addWidget(
            host_label
        )

        layout.addWidget(
            self.host_input
        )

        layout.addWidget(
            port_label
        )

        layout.addWidget(
            self.port_input
        )

        layout.addWidget(
            save_button
        )



        self.setLayout(
            layout
        )