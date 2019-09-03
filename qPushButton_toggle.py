# toggle button

import sys
from PyQt5.QtWidgets import QPushButton, QApplication, QSizePolicy
from PyQt5.QtCore import pyqtSlot

class Button(QPushButton):
    def __init__(self):
        QPushButton.__init__(self, "OFF")
        # self.setFixedSize(100, 100)
        self.setStyleSheet("background-color: pink")

        self.setCheckable(True)
        self.toggled.connect(self.slot_toggle)
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.setMinimumSize(100, 100)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(100)
        size.setWidth(100)
        return size

    def slot_toggle(self, state):
        self.setStyleSheet("background-color: %s" % ({True: "yellow", False: "pink"}[state]))
        self.setText({True: "ON", False: "OFF"}[state])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Button()
    form.show()
    exit(app.exec_())
