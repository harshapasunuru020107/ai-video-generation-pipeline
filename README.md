🎬 AI Video Generation Pipeline

An end-to-end automated AI pipeline that transforms a user-provided topic into a fully rendered, YouTube-ready video.

This system generates:

📝 AI-written script

🔊 AI voiceover

🖼 Relevant stock visuals

🎥 Final rendered MP4 video

All triggered with a single input.

🚀 Demo

🔗 YouTube Demo (Unlisted)
[Paste your YouTube link here]

🎥 End-to-End Execution Recording
[Paste your Google Drive link here]

🧠 Architecture Overview
User Input (Topic)
        ↓
Script Generation (Gemini API)
        ↓
Visual Keyword Extraction
        ↓
Voice Generation (Edge TTS)
        ↓
Visual Fetching (Pexels API)
        ↓
Video Rendering (FFmpeg)
        ↓
Final output.mp4


The system is modular and follows separation of concerns for scalability and maintainability.

🛠 Tech Stack
Component	Tool Used
Script Generation	Gemini API (Free Tier)
Text-to-Speech	Microsoft Edge TTS
Visuals	Pexels API
Video Rendering	FFmpeg
Language	Python

All tools used are free-tier compliant.

📂 Project Structure
ai-video-generation-pipeline/
main.py
script_generator.py
voice_generator.py
visuals_fetcher.py
video_builder.py
requirements.txt
.env.example


Each module handles a single responsibility:

script_generator.py → AI script + keywords

voice_generator.py → Voice synthesis

visuals_fetcher.py → Image retrieval

video_builder.py → FFmpeg rendering

main.py → Orchestrates pipeline

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/harshapasunuru020107/ai-video-generation-pipeline.git
cd ai-video-generation-pipeline

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Add Environment Variables

Create a .env file:

GEMINI_API_KEY=your_key_here
PEXELS_API_KEY=your_key_here

▶️ Usage

Run:

python main.py


Enter a topic when prompted.

The pipeline will:

Generate script

Extract visual keywords

Generate voiceover

Download relevant images

Render final video

Final output:

output.mp4

⚡ Key Challenges Solved

Migrated from deprecated Gemini SDK to google.genai

Handled API rate limits

Resolved FFmpeg “height not divisible by 2” encoding error

Implemented dynamic audio-video synchronization

Ensured full automation without manual editing

🔮 Future Improvements

Auto subtitle (.srt) generation

Auto thumbnail creation

Direct YouTube API upload

Support for multiple LLM providers

Dynamic transitions and zoom effects

📌 Assignment Context

This project was built as part of an AI engineering assignment requiring:

Fully automated end-to-end pipeline

Free tool usage only

Single trigger → YouTube-ready video

Modular architecture

👨‍💻 Author

Harsha Pasunuru
AI & Software Engineering Enthusiast

✅ Final Result

One topic in → One complete video out.
Fully automated. No manual intervention.

