import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QTabWidget, QHBoxLayout, QVBoxLayout, QComboBox, QLabel, QLineEdit)
from PyQt5.QtCore import Qt

class Converter(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lengthTab = QWidget()
        weightTab = QWidget()

        # QTabWidget
        tabs = QTabWidget()
        tabs.addTab(LengthTab(), 'Length Converter')
        tabs.addTab(WeightTab(), 'Weight Converter')

        # boxLayout
        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        # self.setGeometry(300, 300, 300, 200) # X, Y, height, width
        self.setFixedSize(300, 200) # 윈도우 창 크기 고정
        self.show()

# FirstTab
class LengthTab(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.input_le = QLineEdit('1')
        # self.input_le.setPlaceholderText('1')

        # QComboBox
        self.cb = QComboBox(self)
        self.cb.addItem('mm')
        self.cb.addItem('cm')
        self.cb.addItem('m')
        self.cb.addItem('km')

        # QLabel
        self.lbl11 = QLabel('1')
        self.lbl22 = QLabel('0.1')
        self.lbl33 = QLabel('0.001')
        self.lbl44 = QLabel('1e-6')

        self.lbl11.setAlignment(Qt.AlignRight)
        self.lbl22.setAlignment(Qt.AlignRight)
        self.lbl33.setAlignment(Qt.AlignRight)
        self.lbl44.setAlignment(Qt.AlignRight)

        self.lbl1 = QLabel('mm')
        self.lbl2 = QLabel('cm')
        self.lbl3 = QLabel('m')
        self.lbl4 = QLabel('km')

        # label 변경, comboBox 변경 시 동작
        self.input_le.textChanged[str].connect(self.onActivated)
        self.cb.activated[str].connect(self.onActivated)

        # boxLayout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.input_le)
        hbox1.addWidget(self.cb)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lbl11)
        vbox1.addWidget(self.lbl22)
        vbox1.addWidget(self.lbl33)
        vbox1.addWidget(self.lbl44)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.lbl1)
        vbox2.addWidget(self.lbl2)
        vbox2.addWidget(self.lbl3)
        vbox2.addWidget(self.lbl4)
        
        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox2)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(hbox1)
        vbox3.addLayout(hbox2)

        self.setLayout(vbox3)

    def onActivated(self):
        num = int(self.input_le.text())
        cText = self.cb.currentText()

        if cText == 'mm':
            self.lbl11.setText(str(num))
            self.lbl22.setText(str(num * 0.1))
            self.lbl33.setText(str(num * 0.001))
            self.lbl44.setText(str(num * 0.000001))
        elif cText == 'cm':
            self.lbl11.setText(str(num * 10))
            self.lbl22.setText(str(num))
            self.lbl33.setText(str(num * 0.01))
            self.lbl44.setText(str(num * 0.00001))
        elif cText == 'm':
            self.lbl11.setText(str(num * 1000))
            self.lbl22.setText(str(num * 100))
            self.lbl33.setText(str(num * 1))
            self.lbl44.setText(str(num * 0.001))
        elif cText == 'km':
            self.lbl11.setText(str(num * 1000000))
            self.lbl22.setText(str(num * 100000))
            self.lbl33.setText(str(num * 1000))
            self.lbl44.setText(str(num * 1))

class WeightTab(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.input_le = QLineEdit('1')

        self.cb = QComboBox(self)
        self.cb.addItem('mg')
        self.cb.addItem('g')
        self.cb.addItem('kg')
        self.cb.addItem('t')

        self.lbl11 = QLabel('1')
        self.lbl22 = QLabel('0.001')
        self.lbl33 = QLabel('1e-6')
        self.lbl44 = QLabel('10e-10')

        self.lbl11.setAlignment(Qt.AlignRight)
        self.lbl22.setAlignment(Qt.AlignRight)
        self.lbl33.setAlignment(Qt.AlignRight)
        self.lbl44.setAlignment(Qt.AlignRight)

        self.lbl1 = QLabel('mg')
        self.lbl2 = QLabel('g')
        self.lbl3 = QLabel('kg')
        self.lbl4 = QLabel('t')

        self.input_le.textChanged[str].connect(self.onActivated)
        self.cb.activated[str].connect(self.onActivated)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.input_le)
        hbox1.addWidget(self.cb)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(self.lbl11)
        vbox1.addWidget(self.lbl22)
        vbox1.addWidget(self.lbl33)
        vbox1.addWidget(self.lbl44)

        vbox2 = QVBoxLayout()
        vbox2.addWidget(self.lbl1)
        vbox2.addWidget(self.lbl2)
        vbox2.addWidget(self.lbl3)
        vbox2.addWidget(self.lbl4)
        
        hbox2 = QHBoxLayout()
        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox2)

        vbox3 = QVBoxLayout()
        vbox3.addLayout(hbox1)
        vbox3.addLayout(hbox2)

        self.setLayout(vbox3)

    def onActivated(self):
        num = int(self.input_le.text())
        cText = self.cb.currentText()

        if cText == 'mg':
            self.lbl11.setText(str(num))
            self.lbl22.setText(str(num * 0.001))
            self.lbl33.setText(str(num * 0.000001))
            self.lbl44.setText(str(num * 0.0000000001))
        elif cText == 'g':
            self.lbl11.setText(str(num * 1000))
            self.lbl22.setText(str(num))
            self.lbl33.setText(str(num * 0.001))
            self.lbl44.setText(str(num * 0.000001))
        elif cText == 'kg':
            self.lbl11.setText(str(num * 1000000))
            self.lbl22.setText(str(num * 1000))
            self.lbl33.setText(str(num * 1))
            self.lbl44.setText(str(num * 0.001))
        elif cText == 't':
            self.lbl11.setText(str(num * 100000000))
            self.lbl22.setText(str(num * 1000000))
            self.lbl33.setText(str(num * 1000))
            self.lbl44.setText(str(num * 1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Converter()
    sys.exit(app.exec_())

