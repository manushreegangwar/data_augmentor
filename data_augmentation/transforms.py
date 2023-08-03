import logging
from typing import List
import random
from enum import Enum
from itertools import cycle
from PIL import Image, ImageFilter


class Transform(Enum):
    """Enumerates types of image transforms."""

    FILTER = 0
    ROTATE = 1


class Filter(Enum):
    """Enumerates types of image filters."""

    BLUR = 0
    EDGE_ENHANCE = 1
    SHARPEN = 2


class FilterImage(object):
    def __init__(self, filter_type: Filter):
        """Initializes filtering transform.

        Args:
            filter_type: Type of filter to apply.

        """
        self._filter = filter_type

    def __call__(self, img: Image):
        """Applies filter to image.

        Args:
            img: Image to apply the filter on.

        Returns:
            img (PIL.Image): Filtered image.
        """
        logging.debug("Filtering image using {}".format(self._filter.name))

        if img.mode != "RGB":
            img = img.convert("L")
        img = img.filter(get_image_filter(self._filter))
        return img


class RotateImage(object):
    def __init__(self, angle: float):
        """Initializes rotation transform.

        Args:
            angle: Angle of rotation for image.
        """
        self._angle = angle

    def __call__(self, img: Image):
        """Applies rotation to image.

        Args:
            img: Image to be rotated.
            angle: Angle of rotation.

        Returns:
            img: Rotated image by angle.
        """
        logging.debug("Rotating image by {} degrees".format(self._angle))
        img = img.rotate(angle=self._angle)
        return img


def get_image_filter(filter_type: Filter):
    """Returns PIL.ImageFilter for filter type.

    Args:
        filter_type (transforms.Filter): Type of filter.
    """
    filter_dict = {
        Filter.BLUR: ImageFilter.BLUR,
        Filter.EDGE_ENHANCE: ImageFilter.EDGE_ENHANCE,
        Filter.SHARPEN: ImageFilter.SHARPEN,
    }

    if filter_type in filter_dict:
        return filter_dict.get(filter_type)
    else:
        raise ValueError("{} not a valid filter type".format(filter_type))


def generate_transforms(transform_types: List[Transform] = None):
    """Generator function for available image transforms.

    Args:
        transform_types: List of types of transforms to cycle over.
    """
    if transform_types is None:
        transform_types = list(Transform)
    for t in cycle(transform_types):
        if t == Transform.FILTER:
            yield FilterImage(filter_type=Filter(random.randint(0, len(Filter) - 1)))
        elif t == Transform.ROTATE:
            yield RotateImage(angle=random.uniform(0, 90))
        else:
            raise ValueError("{} is an undefined transform type".format(t))


def create_transform_list(
    n_transforms: int, transform_types: List[Transform] | None = None
):
    """Produces a list of N images transforms.

    Args:
        transform_type: List of transforms to use.
    """
    transform_generator = generate_transforms(transform_types)
    image_transforms = [next(transform_generator) for i in range(n_transforms)]

    return image_transforms
