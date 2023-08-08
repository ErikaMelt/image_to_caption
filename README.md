# Image Captioning Project

This project uses a pre-trained transformer model to generate captions for uploaded images. The application is built using Flask and allows users to upload an image and receive an automatic caption for the image.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

- Python 3.8 
- [Pip](https://pip.pypa.io/en/stable/installing/)
- [Virtual environment](https://docs.python.org/3/library/venv.html) (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ErikaMelt/image-captioning-repo.git
   cd your-image-captioning-repo

2. Set up a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate

### Usage

- Run the Flask application:

   ```bash
   python app.py

- Open a web browser and go to http://127.0.0.1:5000/
- Upload an image using the provided form and see the generated caption.

#### Example
<img width="1231" alt="example" src="https://github.com/ErikaMelt/image_to_caption/assets/104458004/19c9d7e8-8d94-4c7a-906b-e43607c5a10f">

### About the Model
The image captioning model used in this project is based on the BlipForConditionalGeneration model from the Transformers library. It generates captions for images using the provided model name.

### Acknowledgments
Model: Salesforce/blip-image-captioning-base from Transformers
Image processing: PIL (Python Imaging Library)
Web framework: Flask
