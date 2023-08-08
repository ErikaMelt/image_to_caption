import os
from flask import Flask, request, render_template, send_from_directory
from transformers import BlipForConditionalGeneration, BlipProcessor
from PIL import Image

app = Flask(__name__)

# Configure the model and processor
model_name = "Salesforce/blip-image-captioning-base"
processor = BlipProcessor.from_pretrained(model_name)
model = BlipForConditionalGeneration.from_pretrained(model_name)

@app.route("/", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        
        file = request.files["file"]
        
        if file.filename == "":
            return "No selected file"
        
        if file:
            filename = os.path.join("static/uploads", file.filename)
            file.save(filename)
            caption = generate_caption(filename)
            return render_template("index.html", caption=caption, image_filename=file.filename)  # Pass just the filename
    
    return render_template("index.html")

@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory("static/uploads", filename)


def generate_caption(image_path):
    with Image.open(image_path) as raw_image:
        rgb_image = raw_image.convert("RGB")
        image_features = processor(images=rgb_image, return_tensors="pt")
        caption = model.generate(**image_features)
        return processor.decode(caption[0], skip_special_tokens=True)

if __name__ == "__main__":
    app.run(debug=True)

