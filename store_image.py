# Store numpy array image on disk
from PIL import Image
import numpy as np

def save_image(image, filename):
    # Convert the image to a PIL image
    image = Image.fromarray(image)
    # Save the image to disk
    image.save(filename)

def open_image(filename):
    # Open the image from disk
    image = Image.open(filename)
    # Convert the image to a numpy array
    image = np.array(image)
    return image