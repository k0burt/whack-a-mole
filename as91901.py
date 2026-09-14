import sys
import time
from random import randint
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt, QTimer

class WhackAMole(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create constant
        self.score_file = "scores.txt"

        # Create variables
        self.score = 0
        self.seconds = 0

        # Create widgets
        self.lbl_score = QLabel(f"Score: {self.score}")
        self.lbl_timer = QLabel(f"Time remaining: {self.seconds}s")
        self.led_timer = QLineEdit(self)
        self.led_timer.setPlaceholderText("Play Time: (s)")

        # Create grid
        self.mole_layout = QGridLayout()
        self.mole_buttons = []
        for row in range(4):
            mole_rows = []
            for col in range(4):
                self.mole = QPushButton(self)
                self.mole.setFixedSize(100, 100)
                self.mole.setStyleSheet(f'background-color: #202020; border-radius: 50%;')
                self.mole.setText("MOLE")
                self.mole.setEnabled(False)
                self.mole_layout.addWidget(self.mole, row, col)
                mole_rows.append(self.mole)
                self.mole.clicked.connect(lambda checked, r=row, c=col: self.mole_clicked(r, c))
            self.mole_buttons.append(mole_rows)

        # Create main layout
        self.v_layout = QVBoxLayout()
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.lbl_score, alignment=Qt.AlignmentFlag.AlignLeft)
        self.h_layout.addStretch()
        self.h_layout.addWidget(self.led_timer)
        self.h_layout.addStretch()
        self.h_layout.addWidget(self.lbl_timer, alignment=Qt.AlignmentFlag.AlignRight)
        self.v_layout.addLayout(self.h_layout)
        self.v_layout.addLayout(self.mole_layout)

        # Display everything
        self.main = QWidget()
        self.main.setLayout(self.v_layout)
        self.cont_main = QWidget()
        self.cont_layout = QVBoxLayout(self.cont_main)
        self.cont_layout.addWidget(self.main, alignment = Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.cont_main)

        self.led_timer.returnPressed.connect(self.led_timer_enter)

    def led_timer_enter(self):
        self.led_timer.hide()
        self.seconds = int(self.led_timer.text())
        self.lbl_timer.setText(f"Time remaining: {self.seconds}s")
        print(self.seconds)
        self.timer_start()
        self.mole_show()

    def mole_clicked(self, row, col):
        # Update score
        self.score += 1
        self.lbl_score.setText(f"Score: {self.score}")

        # Disable clicked mole
        self.mole_buttons[row][col].setEnabled(False)
        self.mole_buttons[row][col].setStyleSheet(f'background-color: #202020; border-radius: 50%;')

        self.mole_show()

    def mole_show(self):
        # Pick random mole
        mole_row = randint(0, 3)
        mole_col = randint(0, 3)

        # Enable random mole
        self.mole_buttons[mole_row][mole_col].setEnabled(True)
        self.mole_buttons[mole_row][mole_col].setStyleSheet(f'background-color: #895129; border-radius: 50%;')

    def timer_start(self):
        # Initiate timer with 1s intervals
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start()

    def update_clock(self):
        self.seconds -= 1
        self.lbl_timer.setText(f"Time remaining: {self.seconds}s")

        # When timer runs out, stop it and run specified function
        if self.seconds == 0:
            self.timer.stop()
            self.timer_done()

    def timer_done(self):
        # Disable all buttons
        for row in range(3):
            for col in range(3):
                self.mole_buttons[row][col].setEnabled(False)
                self.mole_buttons[row][col].setStyleSheet(f'background-color: #202020; border-radius: 50%;')
                self.mole_buttons[row][col].hide()

        # Remove grid and timer, and enlargen score
        self.v_layout.removeItem(self.mole_layout)
        self.h_layout.removeWidget(self.lbl_timer)
        self.lbl_score.setStyleSheet('font-size: 48px')

app = QApplication(sys.argv)
window = WhackAMole()
window.show()
sys.exit(app.exec())