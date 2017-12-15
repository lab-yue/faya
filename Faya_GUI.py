#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import QLineEdit, QWidget, QPushButton, QApplication, QGridLayout, QTextEdit, QLabel
from Faya_fun import scenario


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.arc = QLabel("~")
        self.g = QPushButton("G~")
        self.word = QLineEdit()
        self.status = QLabel("~")

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.arc, 1, 1, 6, 10)
        grid.addWidget(self.word, 7, 1, 1, 3)

        grid.addWidget(self.g, 7, 10)

        grid.addWidget(self.status,7,6)

        self.g.clicked.connect(self.gClicked)

        self.setLayout(grid)

        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('GUI')
        self.show()

    def gClicked(self):

        cmd = self.word.text()

        cooked = ''

        try:
            cooked = scenario('主人', cmd, '')
        except:
            raise

        self.word.clear()

        self.arc.setText(cooked)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())