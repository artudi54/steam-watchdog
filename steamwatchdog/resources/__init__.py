from pathlib import Path

RESOURCE_ICON = str(Path(__file__).resolve().parent / "icon.png")
RESOURCE_AUTOSTATRT = str(Path(__file__).resolve().parent / "steam-watchdog.desktop")

__all__ = ["RESOURCE_ICON", "RESOURCE_AUTOSTATRT"]