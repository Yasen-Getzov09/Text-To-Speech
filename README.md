# Text-to-Speech Python Application

This is a simple Python application that uses the `pyttsx3` library to convert text input into speech. It allows the user to type a sentence or phrase, and the program will speak it aloud. The user can type `quit` to exit the application.

## Features
- **Text-to-Speech**: Converts typed text into speech.
- **Customizable Speech Rate**: You can adjust the rate at which the text is spoken.
- **Voice Selection**: Choose from available voices installed in your system.

## Prerequisites

Before running the project, make sure you have the following installed:

- **Python 3.x**: You can download Python from [here](https://www.python.org/downloads/).
- **pyttsx3**: A Python library that provides text-to-speech capabilities.

To install the required dependencies, run:

## How to Use

1. Clone the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the Python script:
4. You will be prompted to type text. The program will convert it into speech and speak aloud.
5. Type `quit` to exit the program.

## Customizing the Application

- You can change the speaking rate by modifying the `engine.setProperty('rate', 150)` line in the code.
- To change the voice, you can modify the line `engine.setProperty('voice', voices[0].id)`. The index `voices[0].id` can be changed to select different voices available on your system.
