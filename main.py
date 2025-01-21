import os
import json
import base64
from dotenv import load_dotenv
from llamaapi import LlamaAPI

# Load environment variables
load_dotenv()

# Initialize the SDK
llama = LlamaAPI(os.getenv("LLAMA_API_KEY"))

# Path to the image
image_path = "image1.png"

# Read the image file and encode it in base64
with open(image_path, "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

# Build the API request
api_request_json = {
    "model": "llama3.2-11b-vision",
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant that can analyze images and answer questions about them."
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "What is in this image?"},
                {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}
            ]
        }
    ],
    "stream": False,
}

# Execute the Request
response = llama.run(api_request_json)

# Print the response
print(json.dumps(response.json(), indent=2))