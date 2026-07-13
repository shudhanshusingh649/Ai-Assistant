import pyautogui
from datetime import datetime
from app.voice.speech_edge import speak


def take_screenshot():

    speak("Taking Screenshot")

    filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

    image = pyautogui.screenshot()

    image.save(f"screenshots/{filename}")

    speak("Screenshot Saved")