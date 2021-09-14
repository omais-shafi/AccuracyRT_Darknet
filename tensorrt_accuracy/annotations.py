
import os
import sys
import json
import argparse
from tqdm import tqdm
import cv2
import pycuda.autoinit  # This is needed for initializing CUDA driver
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
from progressbar import progressbar

from utils.yolov3 import TrtYOLOv3
from utils.yolov3_classes import yolov3_cls_to_ssd
import numpy as np

HOME = os.environ['HOME']
print (HOME)
VAL_IMGS_DIR = HOME + '/Trafficdata/finalimages/'
VAL_ANNOTATIONS = HOME + '/omais/tensorrt_demos/trafficdata.json'
cocoGt = COCO(VAL_ANNOTATIONS)
#imgIds= sorted(cocoGt.getImgIds())
cocoDt = cocoGt.loadRes('yolov3_onnx/check.json')
imgIds = sorted(cocoGt.getImgIds())
imgIds=imgIds[0:100]
imgId = imgIds[np.random.randint(100)]
cocoEval = COCOeval(cocoGt, cocoDt, 'bbox')
cocoEval.params.imgIds = imgIds
cocoEval.evaluate()
cocoEval.accumulate()
print(cocoEval.summarize())


