#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 10:54:54 2018

@author: sichen
"""
import sys

# define close
def close_application(self):
    choice = QMessageBox.question(self, 'Exit!', 
                                  'Exiting the progrem?',
                                  QMessageBox.Yes | QMessageBox.No)
    if choice == QMessageBox.Yes:
        print('Exiting now!')
        sys.exit()
    else:
        pass
    
