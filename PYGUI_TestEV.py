import logging
import os
import PySimpleGUI as sg
from playsound import playsound

# Set up logging
logging.basicConfig(level=logging.INFO)

def validate_mp3(file_path):
    # Check if file exists and has an .mp3 extension
    if os.path.exists(file_path) and file_path.lower().endswith('.mp3'):
        logging.info(f"Playing MP3 file: {file_path}")
        playsound(file_path)
        return True
    else:
        logging.warning("Invalid MP3 file or file not found.")
        return False

# Define the layout of the main window
main_layout = [
    [sg.Text("Welcome to Study Buddy", font=('Impact', 60))],
    [sg.Text("By: Team QRS", font=('Impact', 20))],
    [sg.Button('Start'), sg.Button('Exit')]
]

# Create the main window
window = sg.Window('Simple', main_layout)

# Event loop for the main window
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Start':
        # Layout for file upload
        file_layout = [
            [sg.Text("Upload an MP3 file:")],
            [sg.Input(), sg.FileBrowse(file_types=(("MP3 Files", "*.mp3"),), key='-MP3_FILE-')],
            [sg.Button('Play'), sg.Button('Cancel')]
        ]
        file_window = sg.Window("MP3 File Upload", file_layout)

        while True:
            file_event, file_values = file_window.read()
            if file_event in (sg.WIN_CLOSED, 'Cancel'):
                file_window.close()
                break
            if file_event == 'Play':
                mp3_file = file_values['-MP3_FILE-']
                if mp3_file:
                    if validate_mp3(mp3_file):
                        sg.Popup("Playing your MP3 file.")
                    else:
                        sg.Popup("Please upload a valid MP3 file.")
                else:
                    sg.Popup("Please upload an MP3 file.")
        file_window.close()

window.close()