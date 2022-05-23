import sys
import os
from PyQt5 import QtGui, QtCore
from Interfaz import*

class Ui_Dialog(QtWidgets.QMainWindow,Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        #-------------------------
        self.pushButton.clicked.connect(self.actualizar)


    def actualizar(self):
        name_archivo = self.lineEdit.text()
        data_archivo = self.lineEdit_2.text()
        number_lines = int(self.lineEdit_3.text())

        self.create(name_archivo, data_archivo, number_lines)
        #self.lineEdit.setText("Acabas de hacer clic en el boton!")
        # escribir       name_archivo = self.lineEdit.setText("")
        self.analize(data_archivo, number_lines)

    def create(self, name, data, lines):
        address = "/Users/godie/Documents/PYTHON/FJ2020/" + name + ".txt"
        f = open (address, 'w')
        for i in range (0, lines):
            f.write(data + "\n")
        f.close()

    def analize(self, data, lines):
        x = ['a', 'e', 'i', 'o', 'u']
        vowels_count = 0
        consonant_count = 0
        for letra in data:
            if letra.lower() in x:
                vowels_count += lines
            else:
                if letra.lower() != " " and letra.lower != "\n":
                     consonant_count += lines               
        self.textBrowser.setText(str(vowels_count))
        self.textBrowser_2.setText(str(consonant_count))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
