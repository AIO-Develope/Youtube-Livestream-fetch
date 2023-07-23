import json
import requests

# Function to retrieve the newest livestream video ID from a YouTube channel
def get_newest_video_id(channel_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={channel_id}&eventType=live&type=video&key={api_key}"
    response = requests.get(url)
    data = response.json()
    if "items" in data and len(data["items"]) > 0:
        return data["items"][0]["id"]["videoId"]
    return None

# Load configuration from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Extract values from the config
channel_id = config["channel_id"]
api_key = config["api_key"]
json_file_path = config["json_file_path"]

# Read the JSON file
with open(json_file_path, "r") as file:
    json_data = json.load(file)

# Get the newest livestream video ID
newest_video_id = get_newest_video_id(channel_id, api_key)

# Find the "Radio" link and update its URL
for link in json_data["links"]:
    if link["label"] == "Radio":
        link["url"] = f"https://www.youtube.com/watch?v={newest_video_id}"
        break

# Write the updated JSON file
with open(json_file_path, "w") as file:
    json.dump(json_data, file, indent=4)
