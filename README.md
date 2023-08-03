# Data Augmentor

## Problem Description
Given a series of images in multiple domains, such as `RGB`, `depth` and `normal`, create augmented datasets by applying transformations, such as `rotation` and `blur`, to images in each domain. For more details, see this [link](https://geoffoxholm.github.io/augmenter/).

## Setup

`conda create -n AUG python=3.11`

`conda activate AUG`

`python setup.py develop`

## Running Augmentor

Before running the script, download the sample data from this [link](https://geoffoxholm.github.io/augmenter/) and save under `data` or a path of your choice.

`python augmentor.py --config-file path/to/config`

## Data Augmentation framework

### 1. `config`
Config parameters are defined as a YAML file for `augmentor`
### 2. `Dataset`
Input images are loaded as `data_augmentation.loader.Dataset`
### 3. `Transform`
Image transforms currently supported are defined in `data_augmentation.transforms`
### 4. `Augment`
To apply a set of image `Transform` to input `Dataset`, use the `data_augmentation.augment.Augment`

## Sample results

Go to `sample_annotations` directory for sample annotations generated using `augmentor.py`

## References

1. [YACS](https://github.com/rbgirshick/yacs)
2. [cocoapi](https://github.com/cocodataset/cocoapi/tree/master/PythonAPI/pycocotools) 

