#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:39:53 2018

@author: sichen
"""

import sys

try:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
   
except:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
    

  
class Window(QMainWindow):
    
    def __init__(self):
        super (Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('XRF Tomo')
        #self.setWindowIcon(QtGui.QIcon(''))
        
        self.creatMenus()
        self.home()
        
#main menu    
    def creatMenus(self):
        
        self.fileMenu = self.menuBar().addMenu("&File")
        #self.fileMenu.addAction(self.newAct)
        #self.fileMenu.addAction(self.openAct)
        #self.fileMenu.addAction(self.saveAct)
        #self.fileMenu.addAction(self.printAct)
        #self.fileMenu.addSeparator()
        #self.fileMenu.addAction(self.exitAct)

        self.editMenu = self.menuBar().addMenu("&Edit")
        #self.editMenu.addAction(self.undoAct)
        #self.editMenu.addAction(self.redoAct)
        #self.editMenu.addSeparator()
        #self.editMenu.addAction(self.cutAct)
        #self.editMenu.addAction(self.copyAct)
        #self.editMenu.addAction(self.pasteAct)
        #self.editMenu.addSeparator()
        
        #extractAction = QAction('&Exit', self)
        #extractAction.setShortcut('Ctrl+Q')
        #extractAction.setStatusTip('Leave the APP')
        #extractAction.triggered.connect(self.close_application)
        
        #self.statusBar()
        
    
# add buttons    
    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        #btn.resize(btn.minimumSizeHint())
        btn.move(100,100)
        self.show()
        
# add methods
    def close_application(self):
        print ('See you next time!')
        sys.exit()
        
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window ()
    sys.exit(app.exec_())


