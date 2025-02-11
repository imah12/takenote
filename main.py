import speech_recognition
import pyautogui
import pyttsx3
import tkinter as tk
from tkinter import filedialog
from speech_engine import listen
from read_notes import read, clear

#to trigger speaking push button
def start_rapping():
    listen()#speech brev

#open txt. file
def open_file():
    file_path = "output.txt"

    with open("output.txt", "r") as file:
        content = file.read()
        text_widget.insert(tk.END, content)#inserts txt. content 


#kill the program (stop talking)
def die_mfer():
    exit()

if __name__ == '__main__':
    print('hello world')

# Create the main application window
root = tk.Tk()
root.title("NOTE-TAKER v1")

# Message label to display status
message_label = tk.Label(root, text="SPEAK CHILD", fg="black")
message_label.pack(pady=10)

#Open txt. file so I can read what I hear
text_widget = tk.Text(root, wrap='word')
text_widget.pack(expand=True, fill="both")

#open button for txt.file(would like to automate)
open_button = tk.Button(root, text="Open txt.", command=open_file)
open_button.pack(pady=10)

#Create the "speak" button
speak_button = tk.Button(root, text="Speak", command=start_rapping)
speak_button.pack()

# Button to open a file
open_button = tk.Button(root, text="Read", command=read)
open_button.pack()

# Button to clear txt. file
open_button = tk.Button(root, text="Clxr", command=clear)
open_button.pack()

#kill switch
kill_switch = tk.Button(root, text='Kill_switxh', command=die_mfer)
kill_switch.pack()

root.mainloop()

