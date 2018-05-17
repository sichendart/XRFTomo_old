#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue May 15 09:39:53 2018

@author: sichen
"""

import sys
from os.path import isfile, join
import string


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
        self.iniUI()
        
    def iniUI(self):
    
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle('XRF Tomo')
        #self.setWindowIcon(QtGui.QIcon(''))
        #self.frame = QFrame()
        #self.vl = QVBoxLayout()
        
        self.createMenus()
        self.home()
        self.show()
        
#main menu    
    def createMenus(self):
        
        opentiffAction = QAction('&Import tiff', self)
        opentiffAction.setStatusTip('Import tiff files')
        opentiffAction.triggered.connect(self.readTiffDir)
        
        openhdfAction = QAction('&Import hdf', self)
        openhdfAction.setStatusTip('Import hdf files')
        openhdfAction.triggered.connect(self.readHDFDir)
        
        saveAction = QAction('&Save', self)
        saveAction.setStatusTip('Save files')
        
        extractAction = QAction('&Exit', self)
        extractAction.setShortcut('Ctrl+Q')
        extractAction.setStatusTip('Leave the APP')
        extractAction.triggered.connect(self.close_application)
        
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
         
        self.ReconMenu = self.menuBar().addMenu("&Reconstruction")
        
        self.ExtraMenu = self.menuBar().addMenu("&Extra")
        
        
# add buttons    
    def home(self):
        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close_application)
        btn.resize(btn.sizeHint())
        btn.move(100,100)
 
#for test       
        testbtn = QPushButton('test', self)
        testbtn.clicked.connect(test_application)
        testbtn.resize(btn.sizeHint())
        #btn.resize(btn.minimumSizeHint())
        testbtn.move(200,100)
        
    def readTiffDir(self):
        """
        To select the directory of the data
        """ 
        path = QFileDialog.getExistingDirectory(self, "Open a folder", 
                                                   QDir.currentPath())
             
    def readHDFDir(self):
        """
        To select the directory that contains h5 files
        """
        try:
            path = QFileDialog.getExistingDirectory(self,"Open a folder",
                                                          QDir.currentPath())                       #type(folderName): <class 'PyQt4.QtCore.QString'
            global RH,fileName
            RH = path
            path = str(path)
            file_name_array = [f for f in os.listdir(path) if isfile(join(path,f))]                  #a list all the file names 
            file_name_array = [f for f in os.listdir(path) if string.find(f,"h5")!=-1]               #a list of only h5 file names
            file_name_array = [path+"/"+f for f in file_name_array]                                  #a list of path/name for the h5 files

            #self.directory = 1
            #self.fileNames = file_name_array
            fileName = file_name_array
            #selectFiles()
        except IndexError:
            print "No folder has been selected."
        except OSError:
            print "No folder has been selected."

# exit    
    def close_application(self):
        choice = QMessageBox.question(self, 'Exit!', 
                                  'Exiting the progrem?',
                                  QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print('Exiting now!')
            sys.exit()
        else:
            pass
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window ()
    sys.exit(app.exec_())


