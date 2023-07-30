from PIL import Image
from matplotlib import pyplot as plt


def show_image(img, fig=None):
    """Displays the given image."""
    if fig is None:
        fig = plt.figure()
    plt.imshow(img)
    plt.show()


def load_image(img_path):
    """Loads image from path."""
    image = Image.open(img_path)
    return image
