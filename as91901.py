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
                self.mole.setStyleSheet('background-color: #202020; border-radius: 50%;')
                self.mole.setEnabled(False)
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

        self.mole_show()

    def mole_clicked(self, row, col):
        # Update score
        self.score += 1
        self.lbl_score.setText(f"Score: {self.score}")

        # Disable clicked mole
        self.mole_buttons[row][col].setEnabled(False)
        self.mole_buttons[row][col].setStyleSheet(f'background-color: #202020; border-radius: 50%;')

        # Show random mole
        self.mole_show()

    def mole_show(self):
        # Pick random mole
        mole_row = randint(0, 3)
        mole_col = randint(0, 3)

        # Enable random mole
        self.mole_buttons[mole_row][mole_col].setEnabled(True)
        self.mole_buttons[mole_row][mole_col].setStyleSheet(f'background-color: #895129; border-radius: 50%;')


app = QApplication(sys.argv)
window = WhackAMole()
window.show()
sys.exit(app.exec())