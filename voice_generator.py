import asyncio
import edge_tts


async def text_to_speech(text, output_file="audio.mp3"):
    communicate = edge_tts.Communicate(
        text,
        "en-US-AriaNeural",
        rate="-5%"
    )
    await communicate.save(output_file)
