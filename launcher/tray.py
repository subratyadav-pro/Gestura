"""System-tray integration."""
from PySide6.QtWidgets import (
    QSystemTrayIcon,
    QMenu,
)
from PySide6.QtGui import QAction


class GesturaTray:

    def __init__(self, ui):

        self.ui = ui

        # Create tray icon
        self.tray = QSystemTrayIcon()

        # You can later replace this with Gestura logo
        self.tray.setIcon(ui.windowIcon())

        # Create menu
        menu = QMenu()

        open_action = QAction("Open Gestura")
        open_action.triggered.connect(self.open_gestura)

        quit_action = QAction("Exit Gestura")
        quit_action.triggered.connect(self.quit_gestura)

        menu.addAction(open_action)
        menu.addSeparator()
        menu.addAction(quit_action)

        self.tray.setContextMenu(menu)

        # Show tray icon
        self.tray.show()

    def open_gestura(self):

        self.ui.showNormal()
        self.ui.raise_()
        self.ui.activateWindow()

    def quit_gestura(self):

        self.tray.hide()
        self.ui.close()