from PyQt5.QtCore import QThread, pyqtSignal
from scripts.recognize import Recognizer

class SpeakThread(QThread):
    append_text_signal = pyqtSignal(str)
    def __init__(self,):
        QThread.__init__(self)
        self.cnt = 0    
        self.rec = Recognizer()
        self.flag = True

    def end(self):
        self.flag = False

    def emit_append_text_signal(self, msg):
        self.append_text_signal.emit(msg)

    def run(self,):
        self.flag = True
        while self.flag:
            self.rec.recognize()

            self.emit_append_text_signal(self.rec.get_txt())