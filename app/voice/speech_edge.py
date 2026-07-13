import asyncio
import edge_tts
import pygame
import os

from app.voice import manager

VOICE = "en-US-JennyNeural"

pygame.mixer.init()

async def generate_voice(text):
    communicate = edge_tts.Communicate(
        text=text,
        voice=VOICE
    )
    await communicate.save("voice.mp3")


def speak(text):

    print(f"NEXA : {text}")

    manager.is_speaking = True
    manager.stop_requested = False
    manager.current_answer = text

    asyncio.run(generate_voice(text))

    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():

        if manager.stop_requested:

            pygame.mixer.music.stop()
            break

        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()

    try:
       if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")
    except PermissionError:
      pass
    manager.is_speaking = False