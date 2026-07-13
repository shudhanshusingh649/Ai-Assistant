from app.core.config import APP_NAME, VERSION
from app.core.logger import logger
from app.voice.speech_edge import speak

def main():
    logger.info("Starting Jarvis AI")

    print("=" * 40)
    print(APP_NAME)
    print(f"Version: {VERSION}")
    print("=" * 40)

    speak("Hello Sir")
    speak("I am Jarvis")
    speak("How can I help you today?")
if __name__ == "__main__":
    main()