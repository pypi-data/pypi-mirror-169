import sys
from PyQt5 import QtGui, QtCore, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, app,
                 args=None,
                 button_height = 20):

        self.app = app
        self.args = args

        super(MainWindow, self).__init__()
        self.setWindowTitle('Physion -- Vision Physiology Software')

        self.setGeometry(50, 100, 500, 500) 
        
        mainMenu = self.menuBar()
        self.fileMenu = mainMenu.addMenu('Experiment')
        self.fileMenu = mainMenu.addMenu('Visualization')
        self.fileMenu = mainMenu.addMenu('Analysis')
        self.fileMenu = mainMenu.addMenu('Others')

        self.show()
        
    def quit(self):
        QtWidgets.QApplication.quit()
        
app = QtWidgets.QApplication(sys.argv)
GUI = MainWindow(app)
sys.exit(app.exec_())

