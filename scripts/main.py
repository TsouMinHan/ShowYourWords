from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import Ui_MainWindow # 導入前端介面檔案
from PyQt5.QtCore import pyqtSignal, Qt ,QThread
from recognize import Recognizer

class Main(QtWidgets.QMainWindow, Ui_MainWindow): # Ui_MainWindow 指的是前端要繼承的class
    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.speak_thread = SpeakThread()
        self.speak_thread.append_text_signal.connect(self.append_text_to_browser)

        self.comboBox.currentTextChanged.connect(self.comboBox_changed)
        self.staartButton.clicked.connect(self.run)  
        self.endButton.clicked.connect(self.end_run)  

    def comboBox_changed(self,):
        # print(self.comboBox.currentText())        
        font_size = int(self.comboBox.currentText())
        self.font.setPointSize(font_size)
        self.textBrowser.setFont(self.font)

    def append_text_to_browser(self, msg):
        self.textBrowser.append(msg)

    def run(self,):
        self.speak_thread.start()

    def end_run(self):
        self.speak_thread.end()

class SpeakThread(QThread):
    append_text_signal = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.cnt = 0    
        self.rec = Recognizer()
        self.flag = True

    def __del__(self):
        self.wait()

    def end(self):
        self.flag = False

    def emit_append_text_signal(self, msg):
        self.append_text_signal.emit(msg)

    def run(self,):
        self.flag = True
        while self.flag:
            self.rec.recognize()

            self.emit_append_text_signal(self.rec.get_txt())

if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow() 
    ui = Main() 
    # ui.setupUi(MainWindow) 
    ui.show() 
    sys.exit(app.exec_())