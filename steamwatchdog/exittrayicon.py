from pathlib import Path
from .resources import *
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QApplication

def find_resource(relative_path: str) -> str:
    return str(Path(__file__).resolve().parent / relative_path)

class ExitTrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        QSystemTrayIcon.__init__(self, parent)
        self.setIcon(QIcon(RESOURCE_ICON))

        menu = QMenu()
        exit_action = menu.addAction('Exit')
        exit_action.triggered.connect(QApplication.instance().quit)
        self.setContextMenu(menu)