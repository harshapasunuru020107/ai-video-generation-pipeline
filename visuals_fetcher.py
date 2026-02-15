import os
import requests
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")


def generate_visual_keywords(topic):
    # Split topic into words
    words = topic.lower().split()

    # Keep meaningful words only
    keywords = [word for word in words if len(word) > 3]

    # Add lifestyle context
    enhanced_keywords = []

    for word in keywords:
        enhanced_keywords.append(f"{word} lifestyle")
        enhanced_keywords.append(f"{word} people")

    # Remove duplicates
    return list(set(enhanced_keywords))[:5]


def fetch_images(query, num_images=1):
    url = "https://api.pexels.com/v1/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": num_images,
        "orientation": "landscape"
    }

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if not os.path.exists("assets"):
        os.makedirs("assets")

    image_paths = []

    for i, photo in enumerate(data.get("photos", [])):
        image_url = photo["src"]["large"]
        image_data = requests.get(image_url).content

        image_path = f"assets/{query.replace(' ', '_')}_{i}.jpg"

        with open(image_path, "wb") as f:
            f.write(image_data)

        image_paths.append(image_path)

    return image_paths
