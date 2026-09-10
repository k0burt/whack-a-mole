import sys
import time
from random import randint
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer

class WhackAMole(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create variables
        self.score = 0

        # Create labels
        self.lbl_score = QLabel(f"Score: {self.score}")

        # Create grid
        self.mole_layout = QGridLayout()
        self.mole_buttons = []
        for row in range(4):
            mole_rows = []
            for col in range(4):
                self.mole = QPushButton(self)
                self.mole.setFixedSize(100, 100)
                self.mole.setStyleSheet('background-color: brown')
                self.mole.setText("MOLE")
                self.mole_layout.addWidget(self.mole, row, col)
                mole_rows.append(self.mole)
                self.mole.clicked.connect(lambda checked, r=row, c=col: self.mole_clicked(r, c))
            self.mole_buttons.append(mole_rows)

        # Create layouts
        self.v_layout =  QVBoxLayout()
        self.v_layout.addWidget(self.lbl_score)
        self.v_layout.addLayout(self.mole_layout)

        # Display everything
        self.main = QWidget()
        self.main.setLayout(self.v_layout)
        self.setCentralWidget(self.main)

    def mole_clicked(self, row, col):
        self.score += 1
        self.lbl_score.setText(f"Score: {self.score}")

app = QApplication(sys.argv)
window = WhackAMole()
window.show()
sys.exit(app.exec())