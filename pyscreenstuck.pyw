#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import pyscreenstuck_engine
from threading import Thread
from PyQt4 import QtGui, QtCore

class InitW(QtGui.QWidget):

	def __init__(self):
		super(InitW, self).__init__()
		self.initUI()
		
	def initUI(self):
		#icon 
		self.setWindowIcon(QtGui.QIcon('logo_small.png')) 
		#logo
		self.pixmap_logo = QtGui.QPixmap("logo_big.png")
		self.lbl_logo = QtGui.QLabel(self)
		self.lbl_logo.setPixmap(self.pixmap_logo)
		#Bottom right buttons
		self.okButton = QtGui.QPushButton("OK")
		self.cancelButton = QtGui.QPushButton("Cancel")
		#Input for email/password/phone/time
		self.emailLabel = QtGui.QLabel('Google Voice Email')
		self.passLabel = QtGui.QLabel('Google Voice Password')
		self.phoneLabel = QtGui.QLabel('Google Voice Number')
		#input fields for email/password/phone/time
		self.emailEdit = QtGui.QLineEdit()
		self.passEdit = QtGui.QLineEdit()
		self.phoneEdit = QtGui.QLineEdit()
		#thread
		self.t = Thread()
		#controller
		self.control = pyscreenstuck_engine.engine()
		#Echo
		self.passEdit.setEchoMode(2)
		
	 
		#Button actions
		#self.cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
		self.cancelButton.clicked.connect(self.quitApp)
		self.okButton.clicked.connect(self.retText)

		#Grid layout
		self.grid = QtGui.QGridLayout() 
		self.grid.setSpacing(10)
		self.grid.addWidget(self.lbl_logo,1,1)
		self.grid.addWidget(self.emailLabel,2,0)
		self.grid.addWidget(self.emailEdit,2,1,1,2)
		self.grid.addWidget(self.passLabel,3,0)
		self.grid.addWidget(self.passEdit,3,1,1,2)
		self.grid.addWidget(self.phoneLabel,4,0)
		self.grid.addWidget(self.phoneEdit,4,1,1,2)
		self.grid.addWidget(self.okButton,5,1)
		self.grid.addWidget(self.cancelButton,5,2)
		self.setLayout(self.grid)
        
		#setting window
		self.setGeometry(300, 300, 300, 150)
		self.setWindowTitle('PyScreenstuck')    
		self.show()

	def clear(self):
		self.grid.removeWidget(self.emailLabel)
		self.emailLabel.deleteLater()
		self.grid.removeWidget(self.emailEdit)
		self.emailEdit.deleteLater()
		self.grid.removeWidget(self.passLabel)
		self.passLabel.deleteLater()
		self.grid.removeWidget(self.passEdit)
		self.passEdit.deleteLater()
		self.grid.removeWidget(self.phoneLabel)
		self.phoneLabel.deleteLater()
		self.grid.removeWidget(self.phoneEdit)
		self.phoneEdit.deleteLater()
		self.grid.removeWidget(self.okButton)
		self.okButton.deleteLater()

		
	def retText(self):
		em = self.emailEdit.text()
		pa = self.passEdit.text()
		ph = self.phoneEdit.text()
		self.clear()
		self.searchLabel = QtGui.QLabel('Checking for updates...')
		self.grid.addWidget(self.lbl_logo,1,2)
		self.grid.addWidget(self.searchLabel,2,2)
		self.grid.addWidget(self.cancelButton,3,2)
		self.grid.setColumnMinimumWidth(3,100)
		self.grid.setColumnMinimumWidth(2,100)
		self.grid.setColumnMinimumWidth(1,100)
		self.t = Thread(target=self.control.setup, args=[em,pa,ph])
		self.t.start()

	def quitApp(self):
		self.control.change()
		self.close()
	    
def main():
    app = QtGui.QApplication(sys.argv)
    ex = InitW()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()