"""
Fingerprint Laptop Unlock System

Professional GUI Styles

PySide6 Dark Theme

Version:
1.0
"""



class AppStyle:
    """
    Central application styling.
    """



    DARK_THEME = """

    /* Main Window */

    QMainWindow {

        background-color: #121212;

    }



    QWidget {

        background-color: #121212;

        color: #FFFFFF;

        font-family: Segoe UI;

        font-size: 14px;

    }



    /* Sidebar */

    QPushButton {

        background-color: #242424;

        color: white;

        border-radius: 8px;

        padding: 12px;

        text-align: left;

    }



    QPushButton:hover {

        background-color: #333333;

    }



    QPushButton:pressed {

        background-color: #0078D7;

    }



    /* Labels */

    QLabel {

        color: #FFFFFF;

    }



    /* Cards */

    QFrame {

        background-color: #1E1E1E;

        border-radius: 12px;

        padding: 15px;

    }



    /* Text Area */

    QTextEdit {

        background-color: #181818;

        color: #DDDDDD;

        border-radius: 8px;

        padding: 10px;

    }



    /* List */

    QListWidget {

        background-color: #181818;

        border-radius: 8px;

        padding: 5px;

    }



    QListWidget::item {

        padding: 10px;

    }



    QListWidget::item:selected {

        background-color: #0078D7;

    }



    /* Input */

    QLineEdit {

        background-color: #242424;

        color: white;

        border-radius: 6px;

        padding: 8px;

    }



    /* Status Bar */

    QStatusBar {

        background-color: #0D0D0D;

        color: #AAAAAA;

    }

    """