import sys
import logging
from pathlib import Path

from .resources import RESOURCE_AUTOSTATRT
from . import SteamWatchdogApplication, SteamWatchdog, ExitTrayIcon


def add_to_autostart(executable: str):
    raw_input = Path(RESOURCE_AUTOSTATRT).read_text("utf-8")
    formatted_input = raw_input.replace("PLACEHOLDER", executable)
    autostart_dir = Path.home() / ".config/autostart"
    autostart_dir.mkdir(parents=True, exist_ok=True)
    destination = autostart_dir / "steam-watchdog.desktop"
    destination.write_text(formatted_input)


def main():
    application = SteamWatchdogApplication(sys.argv)
    logging.info("Application initialized")

    tray_icon = ExitTrayIcon(application)
    tray_icon.show()
    logging.info("Tray icon created")

    add_to_autostart(sys.argv[1])
    logging.info("Added steam-watchdog to autostart")

    steam_watchdog = SteamWatchdog(application)
    steam_watchdog.start(5000)

    exit_code = application.exec()
    logging.info(f"Application exited with code {exit_code}")

    return exit_code

if __name__ == "__main__":
    sys.exit(main())