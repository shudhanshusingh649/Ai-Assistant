import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("🎤 Waiting for 'Hey Nexa'...")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

    try:

        text = recognizer.recognize_google(audio).lower()

        print("You:", text)
        
        print(f"Recognized: {text}")

        return text

    except Exception:

        return ""