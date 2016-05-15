import sys
from PyQt5.QtWidgets import *
from PyQt5.Qt import *



class CreateOrViewProjectMainWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        # self.setStyleSheet("background-image: url(/Users/Chieh/Desktop/EngineerHub/loginPageBackEdit.jpg")
        self.but1 = QPushButton('heyee')
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.but1)

        self.setCentralWidget(self.but1)


        self.show()

