import sys, os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import uic

from PIL import Image
from os.path import expanduser

form_class = uic.loadUiType("imgAug.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.ilist = list()
        
        self.wresizeLine.setDisabled(True)
        self.hresizeLine.setDisabled(True)
        self.rotateLine.setDisabled(True)
        self.prefixLine.setDisabled(True)
        self.suffixLine.setDisabled(True)

        self.resizeCb.stateChanged.connect(self.cbClicked)
        self.rotateCb.stateChanged.connect(self.cbClicked)
        self.renameCb.stateChanged.connect(self.cbClicked)

        self.pathBtn.clicked.connect(self.getPath)

        self.runBtn.clicked.connect(self.runClicked)

    def runClicked(self):
        self.getImageList(self.pathLine.text())
        for i, im in enumerate(self.ilist):
            img = Image.open(self.pathLine.text() + "/" + im)
            
            if self.resizeCb.isChecked():
                width = int(self.wresizeLine.text())
                height = int(self.hresizeLine.text())
                img = img.resize((width, height))
            
            if self.rotateCb.isChecked():
                rotate = int(self.rotateLine.text())
                img = img.rotate(rotate)
            
            if self.hflipCb.isChecked():
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
            
            if self.vflipCb.isChecked():
                img = img.transpose(Image.FLIP_TOP_BOTTOM)

            if self.renameCb.isChecked():
                prefix = self.prefixLine.text()
                suffix = self.suffixLine.text()
                newName = prefix + str(i) + suffix + os.path.splitext(im)[-1]
                img.save(os.path.join(self.pathLine.text(), newName))
            else:
                img.save(os.path.join(self.pathLine.text(), im))
        

    def cbClicked(self, state):
        if self.resizeCb.isChecked():
            self.wresizeLine.setDisabled(False)
            self.hresizeLine.setDisabled(False)
            self.wresizeLine.setText('')
            self.hresizeLine.setText('')
            self.wresizeLine.setFocus()
        else:
            self.wresizeLine.setDisabled(True)
            self.hresizeLine.setDisabled(True)
        
        if self.rotateCb.isChecked():
            self.rotateLine.setDisabled(False)
            self.rotateLine.setFocus()
        else:
            self.rotateLine.setDisabled(True)
        
        if self.renameCb.isChecked():
            self.prefixLine.setDisabled(False)
            self.suffixLine.setDisabled(False)
            self.prefixLine.setFocus()
        else:
            self.prefixLine.setDisabled(True)
            self.suffixLine.setDisabled(True)

    def getPath(self):
        imgdir = QFileDialog.getExistingDirectory(
                self, "Open a folder", expanduser("~"), 
                QFileDialog.ShowDirsOnly)
        self.pathLine.setText(imgdir)

    def getImageList(self, dirname):
        del self.ilist[:]
        imglist = os.listdir(dirname)
        for img in imglist:
            fullImgName = os.path.join(dirname, img)
            ext = os.path.splitext(fullImgName)[-1]
            if ext == '.jpg' or ext == '.png':
                self.ilist.append(os.path.split(fullImgName)[-1])
                print(fullImgName)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
