import os
import subprocess


def get_audio_duration(audio_path):
    result = subprocess.run(
        [
            "ffprobe",
            "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            audio_path
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return float(result.stdout.strip())


def build_video(image_paths, audio_path="audio.mp3", output_path="output.mp4"):
    audio_duration = get_audio_duration(audio_path)

    num_images = len(image_paths)
    duration_per_image = audio_duration / num_images

    # Create image list file
    with open("images.txt", "w", encoding="utf-8") as f:
        for image in image_paths:
            f.write(f"file '{os.path.abspath(image)}'\n")
            f.write(f"duration {duration_per_image}\n")

        # FFmpeg requires last image without duration
        f.write(f"file '{os.path.abspath(image_paths[-1])}'\n")

    # Create slideshow
    subprocess.run([
        "ffmpeg",
        "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", "images.txt",
        "-vf", "scale=1280:720,format=yuv420p",
        "-r", "24",
        "slideshow.mp4"
    ])

    # Combine with audio
    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", "slideshow.mp4",
        "-i", audio_path,
        "-c:v", "libx264",
        "-c:a", "aac",
        "-shortest",
        output_path
    ])

    # Cleanup
    os.remove("images.txt")
    os.remove("slideshow.mp4")

    return output_path
