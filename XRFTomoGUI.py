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

from moreOpts import * 

  
class Window(QMainWindow):
    
    def __init__(self):
        super (Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('XRF Tomo')
        #self.setWindowIcon(QtGui.QIcon(''))
        #self.frame = QFrame()
        #self.vl = QVBoxLayout()
        
        self.createMenus()
        self.home()
        
#main menu    
    def createMenus(self):
        
        opentiffAction = QAction('&Import tiff', self)
        opentiffAction.setStatusTip('Import tiff files')
        opentiffAction.triggered.connect(self.readDir)
        
        openhdfAction = QAction('&Import hdf', self)
        openhdfAction.setStatusTip('Import hdf files')
        openhdfAction.triggered.connect(self.readDir)
        
        saveAction = QAction('&Save', self)
        saveAction.setStatusTip('Save files')
        
        extractAction = QAction('&Exit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the APP')
        extractAction.triggered.connect(close_application)
        
        self.statusBar()
        
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(opentiffAction)
        self.fileMenu.addAction(openhdfAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(saveAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(extractAction)

        
        self.configMenu = self.menuBar().addMenu("&Config")

        self.editMenu = self.menuBar().addMenu("&Edit")
        
        self.AlignMenu = self.menuBar().addMenu("&Alignment")
        
        self.ExtraMenu = self.menuBar().addMenu("&Extra")
         
        self.ReconMenu = self.menuBar().addMenu("&Reconstruction")
        
        
# add buttons    
    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(close_application)
        btn.resize(btn.sizeHint())
        #btn.resize(btn.minimumSizeHint())
        btn.move(100,100)
        self.show()
        


# readTiffStack
    def readDir(self):
        """
        To select the directory of the data
        """ 
        fileDir = QFileDialog.getExistingDirectory(
            self, 
            "Open a folder", 
            QDir.currentPath(),
            QFileDialog.ShowDirsOnly
            )
        print (fileDir)      
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window ()
    sys.exit(app.exec_())


