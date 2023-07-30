import os
from yacs.config import CfgNode as CN


_C = CN()

_C.INPUT = CN()
_C.INPUT.DIR = "data"
_C.INPUT.DOMAINS = ("rgb", "normal", "depth")
_C.INPUT.ANNOTATION_FILE = "annotations_input.json"

_C.TRANSFORM = CN()
_C.TRANSFORM.NUMBER = 0
_C.TRANSFORM.TYPE = ()

_C.OUTPUT = CN()
_C.OUTPUT.DIR = "augmentations_output"
_C.OUTPUT.ANNOTATION_FILE = "annotations_output.json"

cfg = _C