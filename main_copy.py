import sys
import speech_recognition
import pyautogui
import pyttsx3
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit,QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtCore import Qt 
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
        text_widget.setPlainText(content)#inserts txt. content 


#kill the program (stop talking)
def die_mfer():
    exit()

if __name__ == '__main__':
    print('hello world')

#Main Window for note taker fam
class coolMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # window settings
        self.setWindowTitle('NOTE-TAKER v1')
        self.setGeometry(100,100,600,600)
        self.setStyleSheet('background-color: #1e1e1e; color: white;')

        #central widget and layout 
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)

        #message label to display status
        self.message_label = QLabel("Speak Child")
        self.message_label.setFont(QFont("Arial", 16))
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("color: #ffffff;")
        layout.addWidget(self.message_label)

        #text widget to display file contents
        global text_widget #declare as global to use in open_file function
        text_widget = QTextEdit()
        text_widget.setReadOnly(True)
        text_widget.setFont(QFont("Arial", 14))
        text_widget.setStyleSheet("background-color: #333333; color: #ffffff; padding: 10px; border-radius: 8px;")
        layout.addWidget(text_widget)

        #buttons with "class fam"
        button_style = """
            QPushButton {
                background-color: #ffffff;
                color: black;
                padding: 10px;
                border-radius: 8px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0099cc;
            }
        """

        #Open button to open file
        self.open_button = QPushButton("Open")
        self.open_button.setStyleSheet(button_style)
        self.open_button.clicked.connect(open_file)
        layout.addWidget(self.open_button)

        #Speak Button 
        self.speak_button = QPushButton("Speak")
        self.speak_button.setStyleSheet(button_style)
        self.speak_button.clicked.connect(start_rapping)
        layout.addWidget(self.speak_button)

        #Read button to read file
        self.read_button = QPushButton("Read")
        self.read_button.setStyleSheet(button_style)
        self.read_button.clicked.connect(read)
        layout.addWidget(self.read_button)

        #clear button to clear the file
        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet(button_style)
        self.clear_button.clicked.connect(clear)
        layout.addWidget(self.clear_button)

        #kill switch button
        self.kill_switch = QPushButton("Kill Switch")
        self.kill_switch.setStyleSheet(button_style)
        self.kill_switch.clicked.connect(die_mfer)
        layout.addWidget(self.kill_switch)

        #set central widget and layout
        self.setCentralWidget(central_widget)

#run the Note Taker
app = QApplication(sys.argv)
Window = coolMainWindow()
Window.show()
sys.exit(app.exec_())