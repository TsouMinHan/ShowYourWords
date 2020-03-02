from PyQt5.QtCore import QThread, pyqtSignal
from scripts.recognize import Recognizer

class SpeakThread(QThread):
    append_text_signal = pyqtSignal(str)
    statusbar_text_signal = pyqtSignal(str)

    def __init__(self,):
        QThread.__init__(self)
        self.cnt = 0    
        self.rec = Recognizer()
        self.flag = True

    def end(self):
        self.flag = False

    def run(self,):
        self.flag = True
        self.statusbar_text_signal.emit('開始偵測')
        while self.flag:
            self.rec.recognize()

            self.append_text_signal.emit(self.rec.get_txt())
        self.statusbar_text_signal.emit('結束偵測')