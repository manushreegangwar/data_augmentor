import json
import os
import pytest
import shutil
import tempfile
from data_augmentation.loader import load_dataset_from_json
from utils.annotation_utils import create_input_annotation_json


def test_input_annotation_json(input_data_dir, input_domains):
    input_json = os.path.join(input_data_dir, "input_annotations.json")
    create_input_annotation_json(
        data_dir=input_data_dir, image_domains=input_domains, annotation_file=input_json
    )
    with open(input_json, "r") as f:
        json_dict = json.load(f)
        for anno in json_dict["annotations"]:
            assert "img_path" in anno.keys()
            assert "img_id" in anno.keys()
            assert "domain" in anno.keys()


def test_load_dataset_from_json(input_data_dir, input_domains):
    input_json = os.path.join(input_data_dir, "input_annotations.json")
    create_input_annotation_json(
        data_dir=input_data_dir, image_domains=input_domains, annotation_file=input_json
    )
    dataset = load_dataset_from_json(json_path=input_json)
    assert len(dataset.get_image_paths()) == 4
