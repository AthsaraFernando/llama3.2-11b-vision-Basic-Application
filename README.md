# LLAMA Vision Project

This project demonstrates how to use the `llama3.2-11b-vision` model from LlamaAPI to analyze images and answer questions about them. The project includes a Python script that sends an image along with a system prompt and a user query to the API, and then prints the model's response.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup](#setup)
  - [Clone the Repository](#clone-the-repository)
  - [Create a Virtual Environment](#create-a-virtual-environment)
  - [Install Dependencies](#install-dependencies)
  - [Set Up Environment Variables](#set-up-environment-variables)
- [Project Structure](#project-structure)
- [Usage](#usage)
  - [Running the Script](#running-the-script)
  - [Customization](#customization)
    - [Changing the Image](#changing-the-image)
    - [Modifying the Prompts](#modifying-the-prompts)
- [Troubleshooting](#troubleshooting)
  - [Common Issues](#common-issues)
- [License](#license)

## Prerequisites

Before you begin, ensure you have the following:

- Python 3.8 or higher installed on your system.
- A LlamaAPI API key. You can obtain this from the LlamaAPI website.
- An image file (e.g., `image1.png`) to analyze.

## Setup

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/LLAMA-vision.git
cd LLAMA-vision
```

### Create a Virtual Environment

Create a virtual environment to isolate the project dependencies:

```bash
python -m venv venv
```

Activate the virtual environment:

On macOS/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

Install the required Python packages:

```bash
pip install llamaapi python-dotenv
```

Save the dependencies to a `requirements.txt` file:

```bash
pip freeze > requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the project root directory to store your LlamaAPI key:

```bash
echo "LLAMA_API_KEY=your_api_key_here" > .env
```

Replace `your_api_key_here` with your actual LlamaAPI key.

## Project Structure

The project has the following structure:

```
LLAMA-vision/
├── venv/                   # Virtual environment directory
├── .env                    # Environment variables file
├── .gitignore              # Git ignore file
├── requirements.txt        # Project dependencies
├── README.md               # This README file
├── main.py                 # Main Python script
└── image1.png              # Example image file
```

## Usage

### Running the Script

1. Place the image you want to analyze (e.g., `image1.png`) in the project root directory.
2. Run the script:

```bash
python main.py
```

The script will send the image and prompts to the `llama3.2-11b-vision` model and print the response to the console.

### Customization

#### Changing the Image

To analyze a different image:

1. Replace `image1.png` with your desired image file in the project root directory.
2. Update the `image_path` variable in `main.py` to point to the new image file:

```python
image_path = "your_new_image.png"
```

#### Modifying the Prompts

You can customize the system prompt and user query in the `api_request_json` dictionary in `main.py`:

- **System Prompt**: This sets the context for the model.

```python
{
    "role": "system",
    "content": "You are a helpful assistant that can analyze images and answer questions about them."
}
```

- **User Query**: This is the question or instruction you want the model to respond to.

```python
{
    "role": "user",
    "content": [
        {"type": "text", "text": "What is in this image?"},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_data}"}}
    ]
}
```

## Troubleshooting

### Common Issues

**API Key Not Found:**

- Ensure the `.env` file exists and contains the correct `LLAMA_API_KEY`.
- Verify that the `python-dotenv` package is installed.

**Image Not Recognized:**

- Ensure the image file exists in the project root directory.
- Verify that the image is in a supported format (e.g., PNG, JPEG).

**API Errors:**

- Check the API response for error messages.
- Ensure the `llama3.2-11b-vision` model is available and correctly specified.

**Base64 Encoding Issues:**

- Ensure the image data is correctly encoded in base64.
- Add debug statements to verify the base64 string is generated correctly.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
