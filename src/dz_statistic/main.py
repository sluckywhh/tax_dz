# -*- coding: utf-8 -*-

#playctrl.py
#播放控制

from PyQt4 import QtCore
from PyQt4 import QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys,threading

from form_statistic import *
import win32api
import win32event

import taxbase

class InvoiceApp(QApplication):
	def __init__(self, argv):
		QApplication.__init__(self,argv)
		self.main()
		# form_usermgr.UserMgr.instance()

	def main(self):
		self.mainwnd = MainWindow(self)


	def quit(self):

		QtGui.qApp.quit()

import winerror


app = InvoiceApp(sys.argv)
app.exec_()

