from kokoro import KPipeline
import soundfile as sf
import pygame
import os

from app.voice import manager

# Initialize pygame mixer only once
pygame.mixer.init()

# Load Kokoro pipeline
pipeline = KPipeline(lang_code="a")

# Female Voice
VOICE = "af_heart"


def speak(text):

    print(f"NEXA : {text}")

    # Empty text check
    if not text.strip():
        return

    manager.is_speaking = True
    manager.stop_requested = False
    manager.current_answer = text

    try:
        # Generate speech
        generator = pipeline(
            text=text,
            voice=VOICE
        )

        # Save generated audio
        for _, _, audio in generator:
            sf.write("voice.wav", audio, 24000)

        # Play audio
        pygame.mixer.music.load("voice.wav")
        pygame.mixer.music.play()

        # Wait until speaking finishes
        while pygame.mixer.music.get_busy():

            # Stop command
            if manager.stop_requested:
                pygame.mixer.music.stop()
                break

            pygame.time.Clock().tick(20)

    except Exception as e:
        print("❌ Kokoro Error :", e)

    finally:

        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        except:
            pass

        try:
            if os.path.exists("voice.wav"):
                os.remove("voice.wav")
        except:
            pass

        manager.is_speaking = False