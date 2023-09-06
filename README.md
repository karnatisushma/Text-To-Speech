
# Text To Speech

which converts text to voice


## Overview

This Python project provides a simple interface for converting text into speech using text-to-speech (TTS) technology. It allows users to input text, and the program generates an audio file with the spoken version of the text.
## Features

- Convert text into speech.
- Customize voice settings such as pitch, speed, and language.
- Save the generated speech as an audio file.
- Supports multiple languages and voices.
- Easy-to-use command-line interface.


## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your machine.
- Required Python packages, which can be installed using the provided 'requirements.txt' file.
## Usage

1. clone the repository:
```bash
git clone https://github.com/yourusername/text-to-speech.git
```
2. Navigate to the project directory:
```bash
cd text-to-speech
```
3. Install required Python packages:
```bash
pip install -r requirements.txt
```
4. Run the script with your desired text and voice settings:
```bash
python text_to_speech.py --text "Your text here" --voice "VoiceName" --pitch 50 --speed 150 --language "LanguageCode" --output "output.wav"
```
- Replace "Your text here" with the text you want to convert.
- Replace "VoiceName" with the name of the desired voice.
- Adjust the pitch and speed values as needed.
- Replace "LanguageCode" with the language code (e.g., "en-US" for English).
- "output.wav" specifies the output audio file name.
5. The program will generate an audio file with the spoken text in the project directory.


