"""Gestura startup confirmation UI."""

from pathlib import Path
import sys
import launcher_state

from PySide6.QtCore import Qt, QEventLoop
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame,
)


class StartupUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.result = None
        # ==========================================================
        # Assets folder
        # ==========================================================

        self.assets_dir = Path(__file__).resolve().parent / "assets"

        # ==========================================================
        # Window
        # ==========================================================

        self.setWindowTitle("Gestura")
        self.resize(1000, 700)

        # ==========================================================
        # Main widget
        # ==========================================================

        central = QWidget()
        self.setCentralWidget(central)

        central.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
            }
        """)

        # Main vertical layout
        main_layout = QVBoxLayout(central)

        main_layout.setContentsMargins(
            70,     # left
            30,     # top
            70,     # right
            40      # bottom
        )

        main_layout.setSpacing(0)

        # ==========================================================
        # Logo
        # ==========================================================

        logo = QLabel()

        logo_path = self.assets_dir / "gestura_logo.png"

        pixmap = QPixmap(str(logo_path))

        if pixmap.isNull():
            print(f"ERROR: Could not load logo: {logo_path}")
        else:
            pixmap = pixmap.scaled(
                150,
                120,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            logo.setPixmap(pixmap)

        logo.setAlignment(Qt.AlignCenter)

        main_layout.addWidget(logo)

        # ==========================================================
        # Title
        # ==========================================================

        title = QLabel("GESTURA")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            QLabel {
                color: #14213D;
                font-size: 48px;
                font-weight: 700;
                letter-spacing: 6px;
            }
        """)

        main_layout.addWidget(title)

        # ==========================================================
        # Subtitle
        # ==========================================================

        subtitle = QLabel(
            "Vision-Based Gesture and Gaze Interaction System"
        )

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""
            QLabel {
                color: #667085;
                font-size: 20px;
            }
        """)

        main_layout.addWidget(subtitle)

        main_layout.addSpacing(35)

        # ==========================================================
        # Features
        # ==========================================================

        features_layout = QHBoxLayout()

        features_layout.setSpacing(40)

        # ----------------------------------------------------------
        # Hand Gesture
        # ----------------------------------------------------------

        hand = self.create_feature(
            self.assets_dir / "hand_gesture.png",
            "Hand Gesture",
            "Control"
        )

        # ----------------------------------------------------------
        # Eye Gaze
        # ----------------------------------------------------------

        eye = self.create_eye_feature(
            self.assets_dir / "eye_gaze.png",
            "Eye Gaze",
            "Interaction"
        )

        # ----------------------------------------------------------
        # Mouse Control
        # ----------------------------------------------------------

        mouse = self.create_feature(
            self.assets_dir / "mouse_control.png",
            "Intuitive",
            "Mouse Control"
        )

        # ----------------------------------------------------------
        # Add hand
        # ----------------------------------------------------------

        features_layout.addWidget(hand)

        # ----------------------------------------------------------
        # Separator 1
        # ----------------------------------------------------------

        separator1 = QFrame()

        separator1.setFrameShape(QFrame.VLine)

        separator1.setStyleSheet("""
            QFrame {
                color: #E5E7EB;
            }
        """)

        features_layout.addWidget(separator1)

        # ----------------------------------------------------------
        # Add eye
        # ----------------------------------------------------------

        features_layout.addWidget(eye)

        # ----------------------------------------------------------
        # Separator 2
        # ----------------------------------------------------------

        separator2 = QFrame()

        separator2.setFrameShape(QFrame.VLine)

        separator2.setStyleSheet("""
            QFrame {
                color: #E5E7EB;
            }
        """)

        features_layout.addWidget(separator2)

        # ----------------------------------------------------------
        # Add mouse
        # ----------------------------------------------------------

        features_layout.addWidget(mouse)

        main_layout.addLayout(features_layout)

        main_layout.addSpacing(35)

        # ==========================================================
        # Horizontal separator
        # ==========================================================

        line = QFrame()

        line.setFrameShape(QFrame.HLine)

        line.setStyleSheet("""
            QFrame {
                color: #E5E7EB;
            }
        """)

        main_layout.addWidget(line)

        main_layout.addSpacing(30)

        # ==========================================================
        # Question
        # ==========================================================

        question = QLabel("Start Gestura?")

        question.setAlignment(Qt.AlignCenter)

        question.setStyleSheet("""
            QLabel {
                color: #101828;
                font-size: 32px;
                font-weight: 700;
            }
        """)

        main_layout.addWidget(question)

        # ==========================================================
        # Description
        # ==========================================================

        description = QLabel(
            "Use your hand gestures and eye gaze to control your computer."
        )

        description.setAlignment(Qt.AlignCenter)

        description.setStyleSheet("""
            QLabel {
                color: #667085;
                font-size: 18px;
            }
        """)

        main_layout.addWidget(description)

        main_layout.addSpacing(25)

        # ==========================================================
        # Buttons
        # ==========================================================

        buttons_layout = QHBoxLayout()

        buttons_layout.setSpacing(25)

        # ----------------------------------------------------------
        # Start button
        # ----------------------------------------------------------

        self.start_button = QPushButton("▶   Start Gestura")

        self.start_button.setFixedSize(350, 70)

        self.start_button.setCursor(Qt.PointingHandCursor)

        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: #1769FF;
                color: white;
                border: none;
                border-radius: 15px;
                font-size: 20px;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #0D5BE1;
            }

            QPushButton:pressed {
                background-color: #084BBE;
            }
        """)

        self.start_button.clicked.connect(self.start_gestura)

        # ----------------------------------------------------------
        # Close button
        # ----------------------------------------------------------

        self.pause_button = QPushButton("◷   Not Now")

        self.pause_button.setFixedSize(300, 70)

        self.pause_button.setCursor(Qt.PointingHandCursor)

        self.pause_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                color: #101828;
                border: 1px solid #D9E1EC;
                border-radius: 15px;
                font-size: 20px;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #F5F8FC;
            }

            QPushButton:pressed {
                background-color: #E9EEF5;
            }
        """)

        self.pause_button.clicked.connect(self.pause_gestura)

        # ----------------------------------------------------------
        # Add buttons
        # ----------------------------------------------------------

        buttons_layout.addStretch()

        buttons_layout.addWidget(self.start_button)
        buttons_layout.addWidget(self.pause_button)

        buttons_layout.addStretch()

        main_layout.addLayout(buttons_layout)

        # Push everything toward the top
        main_layout.addStretch()

    # ==============================================================
    # Feature Widget
    # ==============================================================

    def create_feature(self, image_path, line1, line2):

        widget = QWidget()

        layout = QVBoxLayout(widget)

        layout.setAlignment(Qt.AlignCenter)

        # ----------------------------------------------------------
        # Icon
        # ----------------------------------------------------------

        icon = QLabel()

        pixmap = QPixmap(str(image_path))

        if pixmap.isNull():
            print(f"ERROR: Could not load image: {image_path}")
        else:
            pixmap = pixmap.scaled(
                100,
                100,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            icon.setPixmap(pixmap)

        icon.setAlignment(Qt.AlignCenter)

        layout.addWidget(icon)

        # ----------------------------------------------------------
        # Text
        # ----------------------------------------------------------

        text = QLabel(
            f"{line1}\n{line2}"
        )

        text.setAlignment(Qt.AlignCenter)

        text.setStyleSheet("""
            QLabel {
                color: #475467;
                font-size: 18px;
            }
        """)

        layout.addWidget(text)

        return widget

    # ==============================================================
    # Eye Feature
    # ==============================================================

    def create_eye_feature(self, image_path, line1, line2):

        widget = QWidget()

        layout = QVBoxLayout(widget)

        layout.setAlignment(Qt.AlignCenter)

        # ----------------------------------------------------------
        # Eye icon
        # ----------------------------------------------------------

        eye = QLabel()

        pixmap = QPixmap(str(image_path))

        if pixmap.isNull():
            print(f"ERROR: Could not load image: {image_path}")
        else:
            pixmap = pixmap.scaled(
                100,
                100,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )

            eye.setPixmap(pixmap)

        eye.setAlignment(Qt.AlignCenter)

        layout.addWidget(eye)

        # ----------------------------------------------------------
        # Text
        # ----------------------------------------------------------

        text = QLabel(
            f"{line1}\n{line2}"
        )

        text.setAlignment(Qt.AlignCenter)

        text.setStyleSheet("""
            QLabel {
                color: #475467;
                font-size: 18px;
            }
        """)

        layout.addWidget(text)

        return widget

    # ==============================================================
    # Start Gestura
    # ==============================================================

    def start_gestura(self):

        print("Starting Gestura...")
        print("Changing state Loading from startup ")
        self.result = True
        self.close()
        
    def pause_gestura(self):
        print("Pausing Gestura....")
        print("changing state paused from startup")
        # self.showMinimized()
        self.result = False
        self.showMinimized()
        
    def run(self):
        self.show()

        loop = QEventLoop()

        self.start_button.clicked.connect(loop.quit)
        self.pause_button.clicked.connect(loop.quit)

        loop.exec()

        return self.result


# ==============================================================
# Application
# ==============================================================

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = StartupUI()

    window.show()

    sys.exit(app.exec())