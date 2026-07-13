import webbrowser
from urllib.parse import quote

from app.voice.speech_edge import speak


def google_search(query):

    speak(f"Searching {query}")

    url = "https://www.google.com/search?q=" + quote(query)

    webbrowser.open(url)
    