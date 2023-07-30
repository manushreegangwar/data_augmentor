from setuptools import setup, find_packages

setup(
    name="data_augmentation",
    version="0.1",
    url="https://github.com/manushreegangwar/data_augmentation",
    description="augment dataset",
    packages=find_packages(exclude=("data")),
)
