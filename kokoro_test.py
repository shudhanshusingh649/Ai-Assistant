from kokoro import KPipeline
import soundfile as sf

pipeline = KPipeline(lang_code="a")

print("Generating voice...")

generator = pipeline(
    "Hello Sudhanshu. I am Nexa. Nice to meet you.",
    voice="af_heart"
)

for i, (gs, ps, audio) in enumerate(generator):
    sf.write(f"output_{i}.wav", audio, 24000)

print("Voice generated successfully")