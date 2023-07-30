from typing import List
import os
import json
import glob
import numpy as np
from collections import defaultdict


def create_input_annotation_json(
    data_dir: str, image_domains: List[str], annotation_file: str
):
    """Creates JSON for input images.

    Args:
        data_dir: Path to input dataset.
        image_domains: List of name of input domains ('rgb', 'depth', 'normal').
        annotation_file: Path to save json to.
    """
    image_annotations = []
    for domain in image_domains:
        domain_images = glob.glob(os.path.join(data_dir, domain, "*.png"))
        for img_path in sorted(domain_images):
            anno = {}
            anno["img_id"] = (img_path.split("/")[-1]).split(".")[0]
            anno["img_path"] = img_path
            anno["domain"] = domain
            image_annotations.append(anno)
    write_annotations(image_annotations, annotation_file)


def write_annotations(image_annotations: List, annotation_file: str):
    """Writes annotations to JSON file.

    Args:
        image_annotations: List of per image annotation.
        annotation_file: Path to save json to.
    """
    data_anno = defaultdict(list)
    data_anno["annotations"] = image_annotations
    with open(annotation_file, "w") as f:
        json.dump(data_anno, f)
