from PyQt5.QtWidgets import QApplication, QMainWindow


from .ui import Ui_MainWindow

class View(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(View, self).__init__(parent)
        self.setupUi(self,)

    def append_text_to_browser(self, msg):
        self.textBrowser.append(msg)

    def comboBox_changed(self,):
        # print(self.comboBox.currentText())        
        font_size = int(self.comboBox.currentText())
        self.font.setPointSize(font_size)
        self.textBrowser.setFont(self.font)
    
    def set_statusbar_text(self, msg):
        self.statusbar.showMessage(msg)