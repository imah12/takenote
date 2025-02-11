import speech_recognition as sr
import pyttsx3
import pyautogui

#create new instance of tts engine
engine = pyttsx3.init()

#engine parameters
engine.setProperty('rate',190)
engine.setProperty('volume',1)

#set engine voice
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

print(voice)

#Text to speech conversion
def speak(text):
    engine.say(text)
    engine.runAndWait()

#initialize the sr_recognizer
r = sr.Recognizer()

#takes user input
def listen():
    with sr.Microphone() as source:
        audio_data = r.listen(source)

    #convert speech to text
    try:
        text = r.recognize_google(audio_data)
        print(text)
        speak(text)

        #save speech transcript to txt.file
        with open("output.txt", "a") as file:
            #write text to file
            file.write(text + "\n")

        if text == "{text} stop" and "stop":
            exit()

    except sr.UnknownValueError:
        print('Speech Recognition could not understand the audio')     
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")







