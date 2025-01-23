#Works with the media folder

import os
import json
import base64
from dotenv import load_dotenv
from llamaapi import LlamaAPI

# Load environment variables
load_dotenv()

# Initialize the SDK
llama = LlamaAPI(os.getenv("LLAMA_API_KEY"))

# Path to the media folder containing images
media_folder = "media"

# Output file to save image descriptions
output_file = "images_details.md"

# Supported image formats
supported_formats = [".png", ".jpg", ".jpeg"]

# Function to process a single image
def process_image(image_path):
    # Extract the image file name
    image_file_name = os.path.basename(image_path)

    # Read the image file and encode it in base64
    with open(image_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode("utf-8")

    # Build the API request
    api_request_json = {
        "model": "llama3.2-11b-vision",
        "messages": [
            {
                "role": "system",
                "content": f"""
You are a highly advanced vision model specialized in analyzing and describing academic images, such as diagrams, tables, charts, and graphs, in extreme detail. Your goal is to provide a thorough and accurate description of the image, ensuring no detail is overlooked. Follow these structured guidelines:

The first line of the output should be the image file name: {image_file_name}

General Overview:
- State the type of image (e.g., ER diagram, table, bar chart).
- Describe its purpose or context if evident.

Structural Details:
- Diagrams (e.g., ER, flowcharts, UML):
  - List all entities, nodes, or components with their labels, attributes, and properties.
  - Explain relationships, connections, directionality, and annotations with each component.
  - Note symbols, colors, or formatting used for meaning.
- Tables:
  - Specify the number of rows and columns.
  - Extract all cell data, noting merged, empty, or specially formatted cells.
  - Describe headers, footers, and annotations.
- Charts/Graphs:
  - Identify the type (e.g., bar chart, line graph).
  - Describe axes, labels, units, scales, and legends.
  - List data points, trends, patterns, and color coding.

Metadata and Formatting:
- Detail layout, orientation, and structure.
- Note text elements (titles, subtitles, captions) and their positions.
- Describe visual elements (borders, gridlines, shading) and embedded symbols or icons.

Contextual Analysis:
- Infer the role or significance of the image in its academic context (e.g., textbook, research paper).
- Highlight key insights or takeaways.

Accuracy and Completeness:
- Ensure exhaustive descriptions with no details omitted.
- Clarify any unclear or ambiguous parts and provide interpretations if possible.

Output should be a logically organized and comprehensive textual description, suitable for academic use.
"""
            },
            {
                "role": "user",
                "content": [
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}
                ]
            }
        ],
        "stream": False,
    }

    # Execute the Request
    response = llama.run(api_request_json)

    # Extract the relevant information
    response_data = response.json()
    description = response_data["choices"][0]["message"]["content"]
    usage = response_data["usage"]

    return description, usage

# Collect all image descriptions
image_descriptions = []

# Iterate through all files in the media folder
for filename in os.listdir(media_folder):
    # Check if the file is a supported image format
    if any(filename.lower().endswith(ext) for ext in supported_formats):
        image_path = os.path.join(media_folder, filename)
        print(f"Processing {filename}...")
        description, usage = process_image(image_path)
        image_descriptions.append(description)
        print(f"Completed processing {filename}.")

# Write all descriptions to the output file
with open(output_file, "w") as md_file:
    for description in image_descriptions:
        md_file.write(description + "\n\n")

print(f"All image descriptions have been saved to {output_file}.")