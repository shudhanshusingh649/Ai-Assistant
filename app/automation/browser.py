import webbrowser

from app.voice.speech_edge import speak


def browser_commands(command):

    command = command.lower()

    if "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "gmail" in command:
        speak("Opening Gmail")
        webbrowser.open("https://mail.google.com")

    else:
        speak("Browser command not found")