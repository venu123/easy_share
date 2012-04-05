#!/usr/bin/python

#system imports
import os
import sys

#my imports
import picasa	#importing picasa.py (contains main picasa function to upload the photo)
import add	#importing add.py which has a function to add the details to the details1.txt

#PyQt imports
from PyQt4.QtCore import *
from PyQt4 import QtGui

 #--------aaargh! globals! ------------
global_uname = " "
global_passwd = " "
global_albumTitle = " "
 #-------------------------------------




#defining the uplod function
def uploadfirst():
 print "uploading!..."  
 #fout=open("countyoutube.txt","r")

 #s1=fout.readline()
 #print s1
 global global_uname
 global global_albumTitle
 global global_passwd
 
 global_uname = str(unameLineEdit.text())
 global_passwd=str(passwdLineEdit.text())
 global_albumTitle=str(albumTitleLineEdit.text())

 #s2="firsttime"
 #if s1==s2:
 fouttest = open("login.log","w")
 fouttest.write("hello1")
       
 s1="notfirsttime"
 f1=open("/home/subrahmanya/countyoutube.txt","w")
#f2=open("/home/subrahmanya/detailsyoutube.txt","r")
 #s1="notfirsttime"
 username=global_uname
 passwrd=global_passwd
 title=global_albumTitle
 filepath=sys.argv[1]
	
	#string1 = "sandeep080"#string1.strip()
	#string2 = "helloWorld"#string2.strip()
	#string3 = sys.argv[2]#:"debug2"#string3.strip()
	#string4 = string4.strip()
	
	#print string1 + "<< uname if"
	#print string2 + "<< upasswd if"
	#print string3 + "<< title if"
	#print string4 + "<< filename if"
	#f2.close()
 f1.write(s1)
	#f2.close()
 f1.close()
	
	
 fouttest.write("hello4")
 fout=open("log.txt","w")
 fout.write(filepath)
 fout.close()
 fouttest.write("hello*")
 print "calling upload! in if"

	#global global_uname
	#string1 = global_uname
	#global global_passwd
	#string2 = global_passwd
	#global global_albumTitle
	#string3 = global_albumTitle
 add.details(username,passwrd)
 print filepath
 print title
 print username
 print passwrd
 picasa.post_to_picasa(filepath,title,username,passwrd)
 print "done!"

 fouttest.write("hello5")
	#sys.exit(app.exec_())
#.............................................................................
def uploadsecond():
	global global_albumTitle
	global_albumTitle=str(albumTitleLineEdit.text())
	f3=open("details1.txt","r")
	username=f3.readline()
	passwrd=f3.readline()
	title=global_albumTitle
	#string5=str(
	filepath=sys.argv[1]
	#string3 = "sandeep080"#string3.strip()
	#string4 = "helloWorld"#string4.strip()
	#string5= sys.argv[2]#"debug5"#string5.strip()
	#stringf= stringf.strip()
	
	#print string3 + "<< uname"
	#print string4 + "<< upasswd"
	#print string5 + "<< title"
	#print stringf + "<< filename"
	#print "calling upload in else"
	
	#global global_uname
	username = username.strip()
	#global global_passwd
	passwrd= passwrd.strip()
	#global global_albumTitle
	#string5 = global_albumTitle
	print filepath
	print title
	print username
	print passwrd
	
	picasa.post_to_picasa(filepath,title,username,passwrd)
        print "done!"




  
#-------------------------
#The logic starts here
fout=open("/home/subrahmanya/count.txt","r")
s1=fout.readline()
print s1
s2="firsttime"
if s1==s2:
  app = QtGui.QApplication(sys.argv)

  win=QtGui.QWidget()   

  grid = QtGui.QGridLayout()
	
  okButton = QtGui.QPushButton("ok")
  cancelButton = QtGui.QPushButton("cancel")

      
  unameLabel = QtGui.QLabel("username")
  passwdLabel = QtGui.QLabel("password")
  albumTitleLabel = QtGui.QLabel("title")

  unameLabel.setToolTip("enter username")
  passwdLabel.setToolTip("enter password")
  albumTitleLabel.setToolTip("enter title")

  grid.addWidget(unameLabel, 3, 2)
  grid.addWidget(passwdLabel,4, 2)
  grid.addWidget(albumTitleLabel,5, 2)
      
  grid.addWidget(okButton,8,5 )
  grid.addWidget(cancelButton,8,6 )

  unameLineEdit = QtGui.QLineEdit()
  global_uname = unameLineEdit
  grid.addWidget(unameLineEdit,3,3 )
      
  passwdLineEdit = QtGui.QLineEdit()
  global_passwd = passwdLineEdit
  passwdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
  grid.addWidget(passwdLineEdit,4,3 )

      
  albumTitleLineEdit = QtGui.QLineEdit()
  global_albumTitle = albumTitleLineEdit
  grid.addWidget(albumTitleLineEdit,5,3)

  win.setLayout(grid) 
  s1="notfirsttime"
  fout=open("/home/subrahmanya/count.txt","w")
  fout.write(s1)
  fout.close()
  
  QObject.connect(okButton,SIGNAL("clicked()"),uploadfirst)
  QObject.connect(cancelButton,SIGNAL("clicked()"),sys.exit)

  win.move(400, 300)
  win.setWindowTitle('easyshare')    
  win.show()	
  sys.exit(app.exec_())
else:
  app = QtGui.QApplication(sys.argv)

  win=QtGui.QWidget()   

  grid = QtGui.QGridLayout()
	
  okButton = QtGui.QPushButton("ok")
  cancelButton = QtGui.QPushButton("cancel")

      
  #unameLabel = QtGui.QLabel("username")
  #passwdLabel = QtGui.QLabel("password")
  albumTitleLabel = QtGui.QLabel("title")

  #unameLabel.setToolTip("enter username")
  #passwdLabel.setToolTip("enter password")
  #albumTitleLabel.setToolTip("enter title")

  #grid.addWidget(unameLabel, 3, 2)
  #grid.addWidget(passwdLabel,4, 2)
  grid.addWidget(albumTitleLabel,5, 2)
      
  grid.addWidget(okButton,8,5 )
  grid.addWidget(cancelButton,8,6 )

  #unameLineEdit = QtGui.QLineEdit()
  #global_uname = unameLineEdit
  #grid.addWidget(unameLineEdit,3,3 )
      
  #passwdLineEdit = QtGui.QLineEdit()
  #global_passwd = passwdLineEdit
  #passwdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
  #grid.addWidget(passwdLineEdit,4,3 )

      
  albumTitleLineEdit = QtGui.QLineEdit()
  global_albumTitle = albumTitleLineEdit
  grid.addWidget(albumTitleLineEdit,5,3)

  win.setLayout(grid) 
  
  QObject.connect(okButton,SIGNAL("clicked()"),uploadsecond)
  QObject.connect(cancelButton,SIGNAL("clicked()"),sys.exit)

  win.move(400, 300)
  win.setWindowTitle('easyshare')    
  win.show()	
  sys.exit(app.exec_())
  
		
