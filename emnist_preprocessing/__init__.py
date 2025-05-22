import numpy as np
from PIL import Image
import io

def preprocess_drawn_image(file_bytes):
    image = Image.open(io.BytesIO(file_bytes)).convert("L")
    image = image.resize((28, 28), Image.LANCZOS)

    image_array = np.array(image).astype(np.float32) / 255.0
    image_array = (image_array < 0.7).astype(np.float32)

    # Optional debug
    Image.fromarray((image_array * 255).astype(np.uint8)).save("debug_input.png")

    return image_array.reshape(1, 28, 28, 1)
