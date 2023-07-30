import os
import logging
import argparse
from config import cfg
from data_augmentation.loader import load_dataset_from_json
from data_augmentation.augment import Augment
from utils.annotation_utils import create_input_annotation_json, write_annotations

logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def main():
    parser = argparse.ArgumentParser(description="Augmenting dataset")
    parser.add_argument(
        "--config-file",
        default="config/config_sample.yaml",
        help="path to config file",
        type=str,
    )
    args = parser.parse_args()

    # Load config parameters
    cfg.merge_from_file(args.config_file)
    cfg.freeze()

    # Read input image domains data
    data_dir = cfg.INPUT.DIR
    input_json_path = os.path.join(data_dir, cfg.INPUT.ANNOTATION_FILE)
    input_domains = cfg.INPUT.DOMAINS

    if not (os.path.exists(input_json_path)):
        # Create annotation json
        logger.info("Creating input annotation JSON")
        create_input_annotation_json(data_dir, input_domains, input_json_path)

    # Generate augmented dataset and annotations
    logger.info("Loading dataset")
    input_dataset = load_dataset_from_json(input_json_path)
    aug = Augment(n_transforms=cfg.TRANSFORM.NUMBER)
    logger.info("Generating augmented dataset")
    image_annotations = aug.generate_annotations(
        dataset=input_dataset, output_dir=cfg.OUTPUT.DIR
    )

    output_json_path = os.path.join(cfg.OUTPUT.DIR, cfg.OUTPUT.ANNOTATION_FILE)
    write_annotations(image_annotations, output_json_path)


if __name__ == "__main__":
    main()
