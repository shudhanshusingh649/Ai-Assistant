import speech_recognition as sr
import time

from app.voice import manager

recognizer = sr.Recognizer()

recognizer.energy_threshold = 400
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8
recognizer.non_speaking_duration = 0.5


def listen():

    # Don't listen while speaking
    while manager.is_speaking:
        time.sleep(0.1)

    with sr.Microphone() as source:

        print("🎤 Waiting for 'Hey Nexa'...")

        # Calibrate microphone only once
        if not hasattr(listen, "_calibrated"):
            recognizer.adjust_for_ambient_noise(source, duration=1)
            listen._calibrated = True

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        except sr.WaitTimeoutError:
            return ""

    try:

        text = recognizer.recognize_google(audio).lower().strip()

        print("You:", text)

        return text

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        print("Speech Recognition Error")
        return ""

    except Exception:
        return "" 