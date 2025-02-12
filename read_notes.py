import pyttsx3
import pyautogui

#create new instance of tts engine
engine = pyttsx3.init()

#engine parameters
engine.setProperty('rate',125)
engine.setProperty('volume',1)

#set engine voice
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

print(voice)

#Text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

#uses speak function to read whats in file
#open txt. file and read
def read():
    with open("output.txt", "r") as file:
        #say whats in file
        speak(file.read())

#clear contents
def clear():
    with open("output.txt", "w") as eraser:
        #erase stuff in file
        pass
