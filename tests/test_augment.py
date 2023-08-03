import pytest
import os
from data_augmentation.augment import Augment
from utils.annotation_utils import create_input_annotation_json
from data_augmentation.loader import load_dataset_from_json


@pytest.fixture
def input_dataset(input_data_dir, input_domains):
    input_json = os.path.join(input_data_dir, "input_annotations.json")
    create_input_annotation_json(
        data_dir=input_data_dir, image_domains=input_domains, annotation_file=input_json
    )
    dataset = load_dataset_from_json(json_path=input_json)
    return dataset


def test_augment_zero():
    with pytest.raises(ValueError):
        aug = Augment(n_transforms=0)


def test_apply_transforms(input_dataset):
    aug = Augment(n_transforms=4)
    transformed_images = aug.apply_transforms(input_dataset.get_image_paths()[0])
    assert len(transformed_images) == 4


@pytest.mark.parametrize("n_transforms", [(2), (3), (4)])
def test_generate_annotations(input_dataset, tmp_path, n_transforms):
    aug = Augment(n_transforms=n_transforms)
    out_annotations = aug.generate_annotations(
        dataset=input_dataset, output_dir=tmp_path
    )
    assert len(out_annotations) == len(input_dataset.get_image_paths()) * n_transforms
