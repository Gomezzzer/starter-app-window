# Random Word Maker

## Overview
The **Random Word Maker** is a simple Python application built with the PyQt5 library. It generates random words from a predefined list and displays them in the interface when buttons are clicked.

## Features
- Displays three labels to show random words.
- Three buttons to generate random words for each label.
- A predefined list of words to randomly choose from.

## Requirements
- Python 3.x
- PyQt5

## Installation

1. **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd random-word-maker
    ```

2. **Install the required libraries:**

    ```sh
    pip install PyQt5
    ```

## Usage

1. **Run the application:**

    ```sh
    python random_word_maker.py
    ```

2. **Interface Overview:**

    - The application window will display a title "Random Keywords".
    - Three labels initialized with "?".
    - Three buttons labeled "Click Me".

3. **Generating Random Words:**

    - Click any of the "Click Me" buttons to generate a random word from the predefined list and display it in the corresponding label.

## Code Overview

### Import Modules
```python
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from random import choice 

