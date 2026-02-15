from script_generator import generate_script
from voice_generator import text_to_speech
from visuals_fetcher import fetch_images
from video_builder import build_video

from dotenv import load_dotenv
import asyncio
import shutil
import os

load_dotenv()

print("AI Video Pipeline Started")

topic = input("Enter video topic: ").strip()

# Clean previous assets
if os.path.exists("assets"):
    shutil.rmtree("assets")

if os.path.exists("output.mp4"):
    os.remove("output.mp4")

# 1️⃣ Generate script
full_output = generate_script(topic)

if not full_output:
    print("Script generation failed.")
    exit()

# 2️⃣ Split script + keywords
if "VISUAL_KEYWORDS:" in full_output:
    script_part, keyword_part = full_output.split("VISUAL_KEYWORDS:")
    script = script_part.strip()

    keywords = list(
        set(
            k.strip()
            for k in keyword_part.split(",")
            if k.strip()
        )
    )
else:
    script = full_output
    keywords = [topic]

# Save script
with open("script.txt", "w", encoding="utf-8") as f:
    f.write(script)

print("Script generated successfully.")
print("Visual Keywords:", keywords)

# 3️⃣ Generate audio
asyncio.run(text_to_speech(script))
print("Audio generated successfully.")

# 4️⃣ Fetch visuals
print("Fetching visuals...")

image_paths = []

for keyword in keywords:
    image_paths.extend(fetch_images(keyword, num_images=1))

print(f"{len(image_paths)} images downloaded successfully.")

if not image_paths:
    print("No images found. Exiting.")
    exit()

# 5️⃣ Build video
print("Building final video...")

build_video(image_paths)

print("🎬 Video created successfully: output.mp4")
