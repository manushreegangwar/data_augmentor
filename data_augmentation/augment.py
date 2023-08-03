from typing import List

import os
import logging
from collections import defaultdict
from data_augmentation.transforms import create_transform_list
from data_augmentation.loader import Dataset
from utils.annotation_utils import write_annotations
from utils.image_utils import load_image


class Augment(object):
    def __init__(self, n_transforms: int):
        """Initializes Augment class.

        Args:
            n_transforms: Number of image transforms.
        """
        if n_transforms <= 0:
            raise ValueError("Number of transforms should be greater than 0.")
        self._transforms = create_transform_list(n_transforms=n_transforms)

    @classmethod
    def from_config(cls, cfg):
        """Initializes Augment from config parameters.

        Args:
            cfg: YACS styled config parameters.
        """
        return cls(n_transforms=cfg.TRANSFORM.NUMBER)

    def apply_transforms(self, image_path: str):
        """Applies transforms to an image.

        Args:
            image_path: Image path
        """
        image = load_image(image_path)
        # TODO: Apply transforms in parallel
        t_images = [image_transform(img=image) for image_transform in self._transforms]
        return t_images

    def generate_annotations(self, dataset: Dataset, output_dir: str):
        """Generates annotations for transformed images in dataset.

        Args:
            dataset (loader.Dataset): Dataset to apply image transforms to.
            output_dir (str): Path to output directory
        """
        image_paths = dataset.get_image_paths()
        os.makedirs(output_dir, exist_ok=True)
        image_annotations = []

        for idx, image_path in enumerate(image_paths):
            logging.info("Applying transforms to image: {}".format(image_path))
            t_images = self.apply_transforms(image_path=image_path)
            root_img_id = dataset.get_image_name(idx)
            root_img_domain = dataset.get_image_domain(idx)

            img_dir = root_img_domain + "-{:0>2d}"
            for i, img in enumerate(t_images):
                img_transform_dir = os.path.join(output_dir, img_dir.format(i))
                os.makedirs(img_transform_dir, exist_ok=True)

                anno = {}
                anno["domain"] = root_img_domain
                anno["img_id"] = str(root_img_id)
                anno["img_path"] = os.path.join(
                    img_transform_dir, anno["img_id"] + str(".png")
                )
                image_annotations.append(anno)

                # Save image to path
                img.save(anno["img_path"])

        return image_annotations
