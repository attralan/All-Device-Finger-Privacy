"""
Fingerprint Laptop Unlock System

Device Management GUI

Version:
4.0
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QInputDialog
)





class DevicePage(QWidget):


    def __init__(
        self,
        controller=None
    ):

        super().__init__()


        self.controller = controller


        self.create_ui()


        self.load_devices()





    def create_ui(self):


        layout = QVBoxLayout()



        title = QLabel(
            "Trusted Devices"
        )


        title.setStyleSheet(

            """
            font-size:24px;
            font-weight:bold;
            """

        )



        self.device_list = QListWidget()



        refresh_button = QPushButton(

            "Refresh"

        )


        pair_button = QPushButton(

            "Pair New Device"

        )


        remove_button = QPushButton(

            "Remove Selected"

        )



        refresh_button.clicked.connect(

            self.load_devices

        )


        pair_button.clicked.connect(

            self.pair_device

        )


        remove_button.clicked.connect(

            self.remove_selected

        )



        buttons = QHBoxLayout()


        buttons.addWidget(refresh_button)

        buttons.addWidget(pair_button)

        buttons.addWidget(remove_button)



        layout.addWidget(title)

        layout.addWidget(self.device_list)

        layout.addLayout(buttons)



        self.setLayout(layout)





    def load_devices(self):


        self.device_list.clear()



        devices = self.controller.get_devices()



        if not devices:


            self.device_list.addItem(

                "No trusted devices"

            )


            return



        for device in devices:


            self.device_list.addItem(

                f"📱 {device[2]} | {device[1]}"

            )





    def pair_device(self):


        device_id, ok = QInputDialog.getText(

            self,

            "Device ID",

            "Enter Android Device ID"

        )



        if not ok or not device_id:


            return



        device_name, ok = QInputDialog.getText(

            self,

            "Device Name",

            "Enter Device Name"

        )



        if not ok:


            return



        public_key, ok = QInputDialog.getText(

            self,

            "Public Key",

            "Enter Public Key"

        )



        if not ok:


            return



        result = self.controller.pair_device(

            device_id,

            device_name,

            public_key

        )



        if result:


            QMessageBox.information(

                self,

                "Success",

                "Device paired successfully"

            )


            self.load_devices()



        else:


            QMessageBox.warning(

                self,

                "Error",

                "Pairing failed"

            )





    def remove_selected(self):


        item = self.device_list.currentItem()



        if not item:


            return



        device_id = item.text().split("|")[-1].strip()



        result = self.controller.remove_device(

            device_id

        )



        if result:


            self.load_devices()