import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt

class KeyPad(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        edit = QLineEdit()
        
        one = QPushButton('1')
        two = QPushButton('2')
        three = QPushButton('3')
        four = QPushButton('4')
        five = QPushButton('5')
        six = QPushButton('6')
        seven = QPushButton('7')
        eight = QPushButton('8')
        nine = QPushButton('9')
        zero = QPushButton('0')
        plus = QPushButton('+')
        enter = QPushButton('enter')
        delete = QPushButton('Del')
        
        btn_list = [one, two, three, four, five, six, seven, eight, nine, zero, plus]

        for i in btn_list:
            i.clicked.connect(lambda state, button = i, edit = edit: self.clickButton(state, button, edit))

        enter.clicked.connect(lambda state, edit = edit: self.answer(state, edit))
        delete.clicked.connect(lambda state, edit = edit: self.one_delete(state, edit))

        hbox1 = QHBoxLayout()
        hbox1.addWidget(seven)
        hbox1.addWidget(eight)
        hbox1.addWidget(nine)
    
        hbox2 = QHBoxLayout()
        hbox2.addWidget(four)
        hbox2.addWidget(five)
        hbox2.addWidget(six)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(one)
        hbox3.addWidget(two)
        hbox3.addWidget(three)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(zero, 2)
        hbox4.addWidget(delete, 1)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(plus, 2)
        vbox1.addWidget(enter, 1)

        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox1)
        vbox2.addLayout(hbox2)
        vbox2.addLayout(hbox3)
        vbox2.addLayout(hbox4)

        hbox5 = QHBoxLayout()
        hbox5.addLayout(vbox2)
        hbox5.addLayout(vbox1)
        
        vbox3 = QVBoxLayout()
        vbox3.addWidget(edit)
        vbox3.addLayout(hbox5)

        self.setLayout(vbox3)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def clickButton(self, state, button, edit):
        exist_line_text = edit.text()
        num_button = button.text()

        edit.setText(exist_line_text + num_button)
    
    def answer(self, state, edit):
        exp = edit.text()
        try:
            edit.setText(str(eval(exp)))
        except:
            edit.setText("wrong")
            
    def one_delete(self, state, edit):
        if edit.text() == "wrong":
            edit.setText('')
        arr = edit.text()
        edit.setText(arr[0:-1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KeyPad()
    sys.exit(app.exec_())

