from PyQt5 import QtWidgets
import sys

from scripts.view import View

class Controller:
    def __init__(self,):
        self._app = QtWidgets.QApplication(sys.argv)
        
        self._view = View()
    
    def run(self,):
        self._view.show()
        return self._app.exec_()