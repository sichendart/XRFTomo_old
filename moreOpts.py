#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:54:54 2018

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

# define selectFiles
def test_application():
    print ('test')
        

        
    return

def readTiffDir(self):
        """
        To select the directory of the data
        """ 
        path = QFileDialog.getExistingDirectory(self, "Open a folder", 
                                                   QDir.currentPath())
    
