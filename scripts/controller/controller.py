from PyQt5 import QtWidgets
import sys

from scripts.view import View
from .speakThread import SpeakThread


class Controller:
    def __init__(self,):
        self._app = QtWidgets.QApplication(sys.argv)
        
        self._view = View()
        self.speak_thread = SpeakThread()

        self.init()

    def init(self,):
        self.speak_thread.append_text_signal.connect(self._view.append_text_to_browser)
        self.speak_thread.statusbar_text_signal.connect(self._view.set_statusbar_text)

        self._view.comboBox.currentTextChanged.connect(self._view.comboBox_changed)
        self._view.startButton.clicked.connect(self.start_speak_thread)  
        self._view.endButton.clicked.connect(self.end_speak_thread)  

    def start_speak_thread(self,):
        self.speak_thread.start()

    def end_speak_thread(self):
        self._view.statusBar().showMessage('關閉麥克風中...(若尚未關閉則是還在偵測中，請隨意說些話結束程式偵測')
        self.speak_thread.end()

    def run(self,):
        self._view.show()
        return self._app.exec_()