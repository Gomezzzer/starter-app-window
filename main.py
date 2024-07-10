from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QMessageBox
from random import choice 

# Main App Objects and Settings
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Random Word Maker")
main_window.resize(300, 200)

# Create all App Objects
title = QLabel("Random Keywords")
text1 = QLabel("?")
text2 = QLabel("?")
text3 = QLabel("?")
button1 = QPushButton("Click Me")
button2 = QPushButton("Click Me")
button3 = QPushButton("Click Me")
input_word = QLineEdit()
add_button = QPushButton("Add Word")
my_words = ['hello', 'goodbye', 'eggs', 'flip', 'horse', 'med', 'sharp', 'lift']

# All Design Here
master_layout = QVBoxLayout()
row1 = QHBoxLayout()
row2 = QHBoxLayout()
row3 = QHBoxLayout()
row4 = QHBoxLayout()

row1.addWidget(title, alignment=Qt.AlignCenter)
row2.addWidget(text1, alignment=Qt.AlignCenter)
row2.addWidget(text2, alignment=Qt.AlignCenter)
row2.addWidget(text3, alignment=Qt.AlignCenter)
row3.addWidget(button1)
row3.addWidget(button2)
row3.addWidget(button3)
row4.addWidget(input_word)
row4.addWidget(add_button)

master_layout.addLayout(row1)
master_layout.addLayout(row2)
master_layout.addLayout(row3)
master_layout.addLayout(row4)
main_window.setLayout(master_layout)

# Create functions 
def random_word1():
    word = choice(my_words)
    text1.setText(word)
    
def random_word2():
    word = choice(my_words)
    text2.setText(word)
    
def random_word3():
    word = choice(my_words)
    text3.setText(word)

def add_word():
    new_word = input_word.text()
    if new_word:
        my_words.append(new_word)
        input_word.clear()
        QMessageBox.information(main_window, "Success", f"Word '{new_word}' added!")
    else:
        QMessageBox.warning(main_window, "Error", "Please enter a word.")

# Events
button1.clicked.connect(random_word1)
button2.clicked.connect(random_word2)
button3.clicked.connect(random_word3)
add_button.clicked.connect(add_word)

# Show/Run our App
main_window.show()
app.exec_()
