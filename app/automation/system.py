import os
from app.voice.speech_edge import speak


def system_commands(command):

    command = command.lower()

    if "chrome" in command:
        speak("Opening Chrome")
        os.system("start chrome")

    elif "notepad" in command:
        speak("Opening Notepad")
        os.system("start notepad")

    elif "calculator" in command:
        speak("Opening Calculator")
        os.system("start calc")

    elif "paint" in command:
        speak("Opening Paint")
        os.system("start mspaint")

    elif "cmd" in command:
        speak("Opening Command Prompt")
        os.system("start cmd")

    elif "explorer" in command or "file explorer" in command:
        speak("Opening File Explorer")
        os.system("start explorer")

    else:
        speak("Application not found.")