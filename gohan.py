import pyaudio
from playsound import playsound
from gtts import gTTS 
import speech_recognition as sr 
import os


record=sr.Recognizer()

def listen(a=False):
    with sr.Microphone() as source:
        if a:
            print(a)
        mic=record.listen(source)
        sound=""

        try:
            sound=record.recognize_google(mic, language="en-EN")
        except sr.UnknownValueError:
            print("Assistant: I DON'T UNDERSTAND YOU")

        except sr.RequestError:
            print("Assistant: System is not working")
        return sound 

def voice(txt):
    tts=gTTS(text=txt,lang="en",slow=False)
    sound="voice.mp3"
    tts.save(sound)
    playsound("voice.mp3")

    os.remove(sound)



def answer(sound):
    if "gohan" in sound:
        voice("hi usame")
        print("Welcome my best friend")
        if "hello" in sound:
            voice("Hi Usame")
            print("hello ")
        if "quit" in sound:
            voice("system is shutting down")
            quit()


print("Hi Usame ")
print("System is opened...")
while True:
    sound=listen()
    if bool(sound)==True:
        print(sound)
        sound=sound.lower()
        answer(sound)
