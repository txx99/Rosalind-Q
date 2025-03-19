# main.py
# how to make an app (prequel to file converter)

#WHEN OPENING IN COMMAND CENTRE:
# preface directions to folder using 'cd' = command-line shell command used to change the current working directory
# HERE "C:\Users\liv_u\OneDrive\Desktop\Py Projx\WelcomeApp"
# THEN WelcomeApp>python main.py


import sys
# sys allows you to manipulate python environment
# can use sys to manipulate output and input 
# stdin (standard input) to get input  from the commad line; standard input
# also sys.stdout and sys.stderr error for whne exceptions occur

import os
# to manipulate operating system / interact with files

import threading
from time import sleep

from time import strftime, gmtime
# gmtime = global timer construct; strftime constructs certain portions of the time as a string using gmtime fucntion
currtime= strftime("%H:%M:%S", gmtime())
# strftime accepts format codes to parse and format dates; format options here https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes



from PyQt6.QtGui import QGuiApplication
# GUI Graphical User Interference  allows user to interact witha  computer program
# QGuiApp is main event loop for processing and dispatching events in a window system in your application
# root window = region of screen where drawing occurs; every window created is within it, forming a hierarchy to the root window;
# all other windows are children or descendent windows

from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal
# unlike quickwindow, appengg does NOT auto create a root window
# appengg more powerful than window

from PyQt6.QtCore import QObject, pyqtSignal


class Backend(QObject):
# object = variables containing data + functions that can be used to manipulate data; like a miniprogram inside python
	def _init_(self):
		QObject._init_(self)
	updated = pyqtSignal(str, arguments=['updater'])
	def updater(self, currtime):
		self.updated.emit(currtime)
#importing QObjects and pyqtSignal; this is called a Signal; one of the few differences between pyqt and pyside (??)
#created a QtObject to receive the Backend object from python
#qml converts py base types into bool (T or F), int, double (float), string(letters), list, QtObject, var

#created pysignal called updated, call it from fucntion updater
#updated argument contains 'updater' function. qml receives data from updater function. in the updater function, we call updated signal and pass currtime data to it

	def bootUp(self):
		t_thread=threading.Thread(target=self._bootUp)
		t_thread.daemon=True
		t_thread.start()
	def _bootUp(self):
		while True:
			currtime=strftime("%H:%M:%S", gmtime())
			self.updater(currtime)
			print(currtime)
			sleep(0.5) #how frequently the time updates from the core program is every 0.1 seconds, so 10x / second
	QQuickWindow.setSceneGraphBackend('software')
#is a fallback option for users with old hardware specs, avoids error
#previously had a property string to receive py currtime str; now created property QtObject to receive py Backend object 

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()
# these two ^^ will use QML for user interface UI layer

engine.quit.connect(app.quit)
# connects UI's quit qith app's quit, so both clsoe whe UI clsoed
# engine.load('C:\Users\liv_u\OneDrive\Desktop\Py Projx\WelcomeApp\main.qml')
engine.load('./UI/main.qml')
back_end = Backend()

engine.rootObjects()[0].setProperty('backend', back_end)
#object back_end created from class Backend
#equated qml backend to pmain py back_end

back_end.bootUp()


engine.rootObjects()[0].setProperty('currTime', currtime) 
# ^ sets currTime variable in qml layer to be equivalent to currtime function in main.py layer -> passing python info to UI layer



#to keep time updating, need to make threads = uses functions or thread calls a function


sys.exit(app.exec())
# app.exec appliation execution = runs the app; 
# is inside sys.exit bc returns exit code which, once passed through sys.exit, exits the system


