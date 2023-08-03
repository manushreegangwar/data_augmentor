import pytest
from data_augmentation.transforms import (
    Transform,
    Filter,
    get_image_filter,
    generate_transforms,
    FilterImage,
    RotateImage,
    create_transform_list,
)
from PIL import Image, ImageFilter, ImageDraw


def test_filter_image(test_image):
    for f_type in list(Filter):
        filter_image = FilterImage(filter_type=f_type)
        out_image = filter_image(test_image)
        assert out_image.size == test_image.size


def test_rotate_image(test_image):
    for r_deg in [-30, 0, 45, 90, 120]:
        rotate_image = RotateImage(angle=r_deg)
        out_image = rotate_image(test_image)
        assert out_image.size == test_image.size


@pytest.mark.parametrize(
    "input_filter, expected_img_filter",
    [
        (Filter.BLUR, ImageFilter.BLUR),
        (Filter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE),
        (Filter.SHARPEN, ImageFilter.SHARPEN),
    ],
)
def test_get_filter(input_filter, expected_img_filter):
    img_filter = get_image_filter(input_filter)
    assert img_filter == expected_img_filter


def test_generate_transforms_filter():
    transform_gen = generate_transforms(transform_types=[Transform.FILTER])
    for i in range(2):
        assert type(next(transform_gen)) == FilterImage


def test_generate_transforms_rotate():
    transform_gen = generate_transforms(transform_types=[Transform.ROTATE])
    for i in range(2):
        assert type(next(transform_gen)) == RotateImage


def test_generate_transforms_none():
    transform_gen = generate_transforms(transform_types=None)
    for i in range(4):
        if i % 2 == 0:
            assert type(next(transform_gen)) == FilterImage
        else:
            assert type(next(transform_gen)) == RotateImage


def test_generate_transforms_invalid():
    transform_gen = generate_transforms(transform_types=["INVALID"])
    with pytest.raises(ValueError):
        next(transform_gen)


@pytest.mark.parametrize(
    "n_transforms, transform_types, expected_transforms",
    [
        (0, None, []),
        (2, [Transform.FILTER], [FilterImage, FilterImage]),
        (2, [Transform.ROTATE], [RotateImage, RotateImage]),
        (4, None, [FilterImage, RotateImage, FilterImage, RotateImage]),
        (4, list(Transform), [FilterImage, RotateImage, FilterImage, RotateImage]),
    ],
)
def test_create_transform_list(n_transforms, transform_types, expected_transforms):
    out_transforms = create_transform_list(
        n_transforms=n_transforms, transform_types=transform_types
    )
    assert all(type(o) == e for o, e in zip(out_transforms, expected_transforms))
