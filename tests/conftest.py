import pytest
from PIL import Image, ImageDraw
import os
import tempfile
import shutil


@pytest.fixture
def output_annotation():
    anno = {
        "annotations": [
            {"img_id": "00", "img_path": "test/rgb-00/00.png", "domain": "rgb"},
            {"img_id": "01", "img_path": "test/rgb-01/01.png", "domain": "rgb"},
            {"img_id": "00", "img_path": "test/depth-00/00.png", "domain": "depth"},
            {"img_id": "01", "img_path": "test/depth-01/01.png", "domain": "depth"},
        ]
    }
    return anno


@pytest.fixture
def rgb_image():
    img = Image.new("RGB", (100, 100))
    draw = ImageDraw.Draw(img)
    draw.rectangle((10, 10, 50, 80), fill="white")
    return img


@pytest.fixture
def gray_image():
    img = Image.new("L", (100, 100))
    draw = ImageDraw.Draw(img)
    draw.rectangle((10, 10, 50, 80), fill="white")
    return img


@pytest.fixture(params=["RGB", "L"])
def test_image(request, rgb_image, gray_image):
    if request.param == "RGB":
        return rgb_image
    elif request.param == "L":
        return gray_image
    else:
        return None


@pytest.fixture
def input_domains():
    return ["rgb", "depth"]


@pytest.fixture
def input_data_dir(input_domains, rgb_image, gray_image):
    dir_path = tempfile.mkdtemp(prefix="test_data", dir=os.getcwd())
    for domain in input_domains:
        domain_dir = os.path.join(dir_path, domain)
        os.makedirs(domain_dir, exist_ok=True)
        for i in range(2):
            img_filepath = os.path.join(domain_dir, f"{i:0>3}.png")
            img = rgb_image if domain == "rgb" else gray_image
            img.save(img_filepath)
    yield dir_path
    shutil.rmtree(dir_path)
