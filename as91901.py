import sys
import time
from random import randint
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer

class WhackAMole(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 300, 300)

        # Create variables
        self.score = 0

        # Create labels
        self.lbl_score = QLabel(f"Score: {self.score}")

        # Create button
        self.mole = QPushButton(self)
        self.mole.setText("MOLE")
        self.mole.setStyleSheet('width: 50px; height: 50px; background-color: brown; border-radius: 50%')
        self.mole.clicked.connect(self.mole_clicked)

        # Create layouts
        self.v_layout =  QVBoxLayout()
        self.v_layout.addWidget(self.lbl_score)
        self.v_layout.addWidget(self.mole)

        # Display everything
        self.main = QWidget()
        self.main.setLayout(self.v_layout)
        self.setCentralWidget(self.main)

    def mole_clicked(self):
        self.score += 1
        self.lbl_score.setText(f"Score: {self.score}")

app = QApplication(sys.argv)
window = WhackAMole()
window.show()
sys.exit(app.exec())