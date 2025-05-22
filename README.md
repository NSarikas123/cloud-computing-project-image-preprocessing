# emnist-preprocessing

Shared preprocessing logic for EMNIST handwritten character recognition.

This module provides a consistent image preprocessing function to be used across both backend inference and training pipelines.

## Installation

```bash
pip install git+https://github.com/NSarikas123/cloud-computing-project-retraining.git
```

## Usage
```bash
from emnist_preprocessing import preprocess_drawn_image

with open("drawing.png", "rb") as f:
    image_bytes = f.read()

processed = preprocess_drawn_image(image_bytes)
# processed shape: (1, 28, 28, 1)
```

## What It Does
- Converts image to grayscale
- Resizes to 28×28
- Normalizes pixel values
- Binarizes (threshold = 0.7)
- Reshapes to model input format