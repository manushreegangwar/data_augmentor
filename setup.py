from setuptools import setup, find_packages

setup(
    name="data_augmentation",
    version="0.1",
    url="https://github.com/manushreegangwar/data_augmentator",
    description="augment dataset",
    packages=find_packages(exclude=("data")),
    install_requires=["numpy", "yacs", "opencv-python", "matplotlib"],
)
