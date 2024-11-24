#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="steam-watchdog",
    version="0.1",
    author="artudi54",
    description="Daemon program to automatically Restart steam when it crashes or closes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/artudi54/steam-watchdog",
    packages=find_packages(),
    package_data={"": ["resources/*.png", "resources/*.desktop"]},
    include_package_data=True,
    scripts=["bin/steam-watchdog"],
    data_files=[("share/icons/hicolor/16x16/apps", ["resources/icons/16x16/steam_watchdog.png"]),
                ("share/icons/hicolor/32x32/apps", ["resources/icons/32x32/steam_watchdog.png"]),
                ("share/icons/hicolor/48x48/apps", ["resources/icons/48x48/steam_watchdog.png"]),
                ("share/icons/hicolor/64x64/apps", ["resources/icons/64x64/steam_watchdog.png"]),
                ("share/icons/hicolor/128x128/apps", ["resources/icons/128x128/steam_watchdog.png"]),
                ("share/icons/hicolor/256x256/apps", ["resources/icons/256x256/steam_watchdog.png"]),
                ("share/icons/hicolor/512x512/apps", ["resources/icons/512x512/steam_watchdog.png"]),
                ("share/applications", ["resources/steam-watchdog.desktop"]),
                ],
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: POSIX :: Linux"],
)
