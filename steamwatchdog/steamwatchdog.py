import logging
import os
import pathlib
import subprocess

from PySide6.QtCore import QTimer, QObject


class SteamWatchdog(QObject):
    def __init__(self, parent: QObject = None) -> None:
        super().__init__(parent)

    def start(self, interval_ms: int) -> None:
        timer = QTimer(self)
        timer.setInterval(interval_ms)
        timer.timeout.connect(SteamWatchdog.__execute_check)
        timer.start()
        logging.info("Started watchdog service")

    @staticmethod
    def __execute_check() -> None:
        if SteamWatchdog.__is_steam_running():
            logging.debug("Steam is running, not doing anything")
            return

        logging.info("Steam is not running, restarting")
        subprocess.Popen(["steam"], preexec_fn=os.setsid, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    @staticmethod
    def __is_steam_running() -> bool:
        pid_file = pathlib.Path.home() / ".steampid"
        if not pid_file.exists():
            return False
        pid = int(pid_file.read_text("utf-8").strip())
        try:
            with open(f"/proc/{pid}/cmdline", "r") as f:
                return "steam" in f.readline()
        except FileNotFoundError:
            return False
        except OSError | RuntimeError:
            logging.error(f"An error occurred while checking if Steam is running")
            return False
