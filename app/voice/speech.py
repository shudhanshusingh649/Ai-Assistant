import os
import uuid

from kokoro import KPipeline
import soundfile as sf
import pygame

from app.voice import manager

# Initialize pygame mixer only once
pygame.mixer.init()

# Load Kokoro pipeline
pipeline = KPipeline(
    repo_id="hexgrad/Kokoro-82M",
    lang_code="a"
)

# Female Voice
VOICE = "af_heart"


def speak(text):

    print(f"NEXA : {text}")

    # Ignore empty text
    if not text.strip():
        return

    manager.is_speaking = True
    manager.stop_requested = False
    manager.current_answer = text

    # Unique filename every time
    filename = f"{uuid.uuid4()}.wav"

    try:

        # Generate speech
        generator = pipeline(
            text=text,
            voice=VOICE
        )

        # Save audio
        for _, _, audio in generator:
            sf.write(filename, audio, 24000)

        # Play audio
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # Wait until speaking finishes
        while pygame.mixer.music.get_busy():

            if manager.stop_requested:
                pygame.mixer.music.stop()
                break

            pygame.time.Clock().tick(20)

    except Exception as e:

        print("❌ Kokoro Error:", e)

    finally:

        try:
            pygame.mixer.music.stop()
        except:
            pass

        try:
            pygame.mixer.music.unload()
        except:
            pass

        try:
            if os.path.exists(filename):
                os.remove(filename)
        except:
            pass

        manager.is_speaking = False