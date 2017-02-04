from PyQt4 import QtCore, QtGui
from sys import *

application = QtGui.QApplication (argv);

window = QtGui.QWidget ();
window.setWindowTitle ("Sample Program");
window.resize (250, 100);

label = QtGui.QLabel ('<h1>Hello, <span style="color: red">my friend</span></h1>');

button1 = QtGui.QPushButton ('Close');

layout = QtGui.QVBoxLayout ();
layout.addWidget (label);
layout.addWidget (button1);


window.setLayout (layout);

QtCore.QObject.connect (button1, QtCore.SIGNAL ('clicked()'), QtGui.qApp, QtCore.SLOT ('quit()'));

window.show ();
exit (application.exec_ ());
