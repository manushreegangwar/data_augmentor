import os
import json
from typing import List, Dict


def load_dataset_from_json(json_path: str):
    """Read annotations from JSON file.

    Args:
        json_path: Path to input JSON annotations.

    Returns:
        Dataset object created using annotations from input JSON file.

    Raises:
        ValueError: An error due to invalid JSON path.
    """

    if not os.path.exists(json_path) or not json_path.endswith(".json"):
        raise ValueError(f"Invalid input JSON path: {json_path}")

    with open(json_path, "r") as f:
        json_dict = json.load(f)

    image_paths = []
    anno_id_to_image_name = dict()
    anno_id_to_domain = dict()

    for idx, anno in enumerate(json_dict["annotations"]):
        image_paths.append(anno["img_path"])
        anno_id_to_image_name[idx] = anno["img_id"]
        anno_id_to_domain[idx] = anno["domain"]

    return Dataset(
        image_paths=image_paths,
        anno_id_to_image_name=anno_id_to_image_name,
        anno_id_to_domain=anno_id_to_domain,
    )


class Dataset:
    """Dataset containing image paths and their respective domains.

    Attributes:
        image_paths: List of image path corresponding to each annotation.
        anno_id_to_image_name: Mapping of annotation index to image filename.
        anno_id_to_domain: Mapping of annotation index to domain.
    """

    def __init__(
        self,
        image_paths: List[str],
        anno_id_to_image_name: Dict,
        anno_id_to_domain: Dict,
    ):
        """Initializes Dataset class.

        Args:
            image_paths: List of image paths
            anno_id_to_image_name: Mapping of annotation index to image filename.
            anno_id_to_domain: Mapping of annotation index to domain.
        """
        self._image_paths = image_paths
        self._anno_id_to_image_name = anno_id_to_image_name
        self._anno_id_to_domain = anno_id_to_domain

    def get_image_paths(self) -> List:
        """Fetches all images in dataset.

        Args:
            load_all (bool): If True, loads all images else returns paths.

        Returns:
            List of image paths
        """
        return self._image_paths

    def get_image_name(self, idx: int) -> str:
        """Returns image filename by annotation index."""
        return self._anno_id_to_image_name.get(idx)

    def get_image_domain(self, idx: int) -> str:
        """Returns image domain by annotation index."""
        return self._anno_id_to_domain.get(idx)
