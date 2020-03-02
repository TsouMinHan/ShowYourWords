from gtts import gTTS
from pygame import mixer
import tempfile
import speech_recognition

class Recognizer():
    def __init__(self,):
        self.r = speech_recognition.Recognizer()

    def recognize(self,):
        with speech_recognition.Microphone() as source:
            print("校準麥克風...")
            self.r.adjust_for_ambient_noise(source)
            print("說些什麼吧!")
            self.audio = self.r.listen(source)

    def get_txt(self,):
        try:
            print("Google Speech Recognition 認為你說:")
            ans = self.r.recognize_google(self.audio, language="zh-TW")
            return ans

        except speech_recognition.UnknownValueError:
            print("Google Speech Recognition 無法理解你說什麼")

        except speech_recognition.RequestError as e:
            print("沒有回應 Google Speech Recognition service: {0}".format(e)) 
        
        return

if __name__ == "__main__":
    
    rec = Recognizer()
    for i in range(10):
        rec.recognize()
        print(rec.get_txt())