import logging
import signal
import sys

from PySide6.QtWidgets import QApplication

class SteamWatchdogApplication(QApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__setup_logger()
        self.__setup_signals()
        self.setQuitOnLastWindowClosed(False)
        self.setApplicationName("Steam Watchdog")

    @staticmethod
    def __setup_logger():
        # output to stdout
        logging.basicConfig(format='[%(asctime)s][%(name)s][%(levelname)s] %(message)s', level=logging.INFO, stream=sys.stdout)

    @staticmethod
    def __setup_signals():
        signal.signal(signal.SIGINT, signal.SIG_DFL)