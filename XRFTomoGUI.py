import sys
from PyQt4 import QtGui, QtCore

Class Window(QtGui.QMainWindow)
  def __init__(self)
      super(Window, self).__init__()
      self.setGeometry(50,50, 300)
      self.setWindowTitle("XRF Tomo")
      
      extractAction = QtGui.QAction('&Exit',self)
      extractAction.setShortcut('Ctrl+Q')
      extractAction.setStatusTip('Leave the program')
      
      self.statusBar()
      
      mainMenu = self.menuBar()
      fileMenu = mainMenu.addMenu('&File')
      fileMenu.addAction(extactAction)
      
      
if __name__ == '__main__':
  app = QtGui.QApplication(sys.argv)
  GUI = Window()
  sys.exit(app.exec_())
