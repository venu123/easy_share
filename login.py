#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtCore import *
from PyQt4 import QtGui
import add



#class Example(QtGui.QWidget):


    #def __init__(self):
        #super(Example, self).__init__()
        
        #self.initUI()
        
    #def initUI(self)
class A(QObject):
	def __init__(self,ledit,ledit1,ledit2):
		global le
		global le1
		global le2
		le=ledit
		le1=ledit1
		le2=ledit2
		QObject.__init__(self)
		
		
	def show(self):
		usr=le.text()
		password=le1.text()
		title=le2.text()
		
		add.details(usr,password,title)
	        	
		
def main():
        fouttest = open("login.log","w")
        fouttest.write("hello")
	
	app = QtGui.QApplication(sys.argv)
        win=QtGui.QWidget()   
           
           #sys.exit(app.exec_())

        
	grid = QtGui.QGridLayout()
	    #app=QApplication(sys.argv)
        
	button = QtGui.QPushButton("ok")
	button1= QtGui.QPushButton("cancel")

	    
	label=QtGui.QLabel("username")
	label1=QtGui.QLabel("password")
	label2=QtGui.QLabel("title")
        label.setToolTip("enter username")
        grid.addWidget(label, 3, 2)
	grid.addWidget(label1,4, 2)
	grid.addWidget(label2,5, 2)
	label.setToolTip("enter username")
	    

        grid.addWidget(button,8,5 )
	grid.addWidget(button1,8,6 )

        lineedit=QtGui.QLineEdit()
	l1=lineedit
	#lineedit.setEchoMode(QtGui.QLineEdit.Password)
	grid.addWidget(lineedit,3,3 )
	    	
	    
	lineedit1=QtGui.QLineEdit()
	l2=lineedit1
	lineedit1.setEchoMode(QtGui.QLineEdit.Password)
        grid.addWidget(lineedit1,4,3 )
	    #QGridLayout.setGeometry(grid,300,280,170)
       
        lineedit3=QtGui.QLineEdit()
        l3=lineedit3
        grid.addWidget(lineedit3,5,3)


        win.setLayout(grid) 
            #self.connect(app.button,SIGNAL("clicked()"),app.button,SLOT("self.show"))
	a=A(l1,l2,l3)
	 
	QObject.connect(button,SIGNAL("clicked()"),a.show)
	        
        win.move(400, 300)
        win.setWindowTitle('easyshare')    
        win.show()
        sys.exit(app.exec_())


        


    
    #app = QtGui.QApplication(sys.argv)
    #ex=Example()
    #ex.initUI()
    #sys.exit(app.exec_())

if __name__ == '__main__':
            main()






















