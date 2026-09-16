import sys


from PySide6.QtWidgets import QApplication


from gui.main_window import MainWindow


from gui.styles import AppStyle


from application.controller import ApplicationController




app = QApplication(sys.argv)



app.setStyleSheet(
    AppStyle.DARK_THEME
)



controller = ApplicationController(
    None
)



window = MainWindow(
    controller
)



window.show()



sys.exit(
    app.exec()
)