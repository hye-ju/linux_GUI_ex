import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QGridLayout, QLayout, QSizePolicy
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
        enter.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        delete = QPushButton('Del')
        delete.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        
        btn_list = [one, two, three, four, five, six, seven, eight, nine, zero, plus]

        for i in btn_list:
            i.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
            i.clicked.connect(lambda state, button = i, edit = edit: self.digitClicked(state, button, edit))

        enter.clicked.connect(lambda state, edit = edit: self.answer(state, edit))
        delete.clicked.connect(lambda state, edit = edit: self.oneDelete(state, edit))

        # Layout

        grid = QGridLayout()
        grid.setSizeConstraint(QLayout.SetNoConstraint)
        self.setLayout(grid)

        grid.addWidget(edit,    0, 0, 1, 4)
        
        grid.addWidget(seven,   1, 0, 1, 1)
        grid.addWidget(eight,   1, 1, 1, 1)
        grid.addWidget(nine,    1, 2, 1, 1)

        grid.addWidget(four,    2, 0, 1, 1)
        grid.addWidget(five,    2, 1, 1, 1)
        grid.addWidget(six,     2, 2, 1, 1)
        
        grid.addWidget(one,     3, 0, 1, 1)
        grid.addWidget(two,     3, 1, 1, 1)
        grid.addWidget(three,   3, 2, 1 ,1)

        grid.addWidget(zero,    4, 0, 1, 2)
        grid.addWidget(delete,  4, 2, 1, 1)
        
        grid.addWidget(plus,    1, 3, 2, 1)
        grid.addWidget(enter,   3, 3, 2, 1)

        self.setWindowTitle('Grid Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


    def digitClicked(self, state, button, edit):
        exist_line_text = edit.text()
        num_button = button.text()

        edit.setText(exist_line_text + num_button)
    
    def answer(self, state, edit):
        exp = edit.text()
        try:
            edit.setText(str(eval(exp)))
        except:
            edit.setText("wrong")
            
    def oneDelete(self, state, edit):
        if edit.text() == "wrong":
            edit.setText('')
        arr = edit.text()
        edit.setText(arr[0:-1])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KeyPad()
    sys.exit(app.exec_())

