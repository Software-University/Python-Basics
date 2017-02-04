#!/usr/bin/env python
from sys import *
from PyQt4 import QtCore, QtGui

application = QtGui.QApplication (argv)

width = 750
height = 185

window = QtGui.QWidget ()
window.setWindowTitle ("Sample Program")
window.resize (width, height)

startX = 20
startY = 20

label = QtGui.QLabel ('<h1>Please input 2 numbers.</h1>', window)
label.move (startX + 0, startY + 0)
label.resize (420, 60)

number1 = QtGui.QTextEdit (window)
number1.move (startY + 0, startY + 60)
number1.resize (210, 30);

plus_sign = QtGui.QLabel ("<h1>+</h1>", window)
plus_sign.move (startY + 220, startY + 60)
plus_sign.resize (20, 30)

number2 = QtGui.QTextEdit (window)
number2.move (startY + 250, startY + 60)
number2.resize (210, 30);

equal_sign = QtGui.QLabel ("<h1>=</h1>", window)
equal_sign.move (startY + 470, startY + 60)
equal_sign.resize (20, 30)

result = QtGui.QLineEdit (window)
result.setReadOnly (1)
result.move (startY + 500, startY + 60)
result.resize (210, 30);

button1 = QtGui.QPushButton ('Calculate', window)
button1.move (startY + 0, startY + 130);
button1.resize (width - startX * 2, 30);

def calc ():
    try:
        result.setText (str (int (number1.toPlainText ()) + int (number2.toPlainText())))
    except:
        result.setText ("Error")

button1.clicked.connect (calc)

window.show ()
exit (application.exec_ ());
