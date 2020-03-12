from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui

import json
from .ui import Ui_MainWindow

class View(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(View, self).__init__(parent)
        self.setupUi(self,)
        self.init()
    
    def init(self):
        ls = [str(i) for i in range(10, 50, 2)]    # 設定字的大小
        self.comboBox.addItems(ls)    
        
        with open ('languages.json', 'r', encoding='utf8') as f:
            language_dc = json.load(f)

        for language in language_dc:
            self.comboBox_2.addItem(language)

    def append_text_to_browser(self, msg):
        self.textBrowser.append(msg)

    def comboBox_changed(self,):      
        font_size = int(self.comboBox.currentText())
        font = QtGui.QFont()
        font.setPointSize(font_size)
        self.textBrowser.setFont(font)
    
    def set_statusbar_text(self, msg):
        self.statusbar.showMessage(msg)