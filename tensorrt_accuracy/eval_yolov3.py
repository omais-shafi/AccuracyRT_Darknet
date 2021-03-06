"""eval_yolov3.py

This script is for evaluating mAP (accuracy) of YOLOv3 models.
"""


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


HOME = os.environ['HOME']
print (HOME)
VAL_IMGS_DIR = HOME + '/finalimages/'
VAL_ANNOTATIONS = HOME + '/traffic.json'


def parse_args():
    """Parse input arguments."""
    desc = 'Evaluate mAP of SSD model'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--imgs_dir', type=str, default=VAL_IMGS_DIR,
                        help='directory of validation images [%s]' % VAL_IMGS_DIR)
    parser.add_argument('--annotations', type=str, default=VAL_ANNOTATIONS,
                        help='groundtruth annotations [%s]' % VAL_ANNOTATIONS)
    parser.add_argument('--model', type=str, default='yolov3-tiny-416',
                        choices=['yolov3-288', 'yolov3-416', 'yolov3-608',
                                 'yolov3-tiny-288', 'yolov3-tiny-416'])
    args = parser.parse_args()
    return args


def check_args(args):
    """Check and make sure command-line arguments are valid."""
    if not os.path.isdir(args.imgs_dir):
        sys.exit('%s is not a valid directory' % args.imgs_dir)
    if not os.path.isfile(args.annotations):
        sys.exit('%s is not a valid file' % args.annotations)


def generate_results(yolov3, imgs_dir, jpgs, results_file):
    """Run detection on each jpg and write results to file."""
    results = []
    var=0
    #print("Called once")
    for jpg in tqdm(jpgs):
        img = cv2.imread(os.path.join(imgs_dir, jpg))
        image_id = jpg.split('.')[0]
       # print("This is here")
       # print (image_id)
        boxes, confs, clss = yolov3.detect(img, conf_th=1e-2)
       # print (clss)
        for box, conf, cls in zip(boxes, confs, clss):
            x = float(box[0])
            y = float(box[1])
            w= float(box[2])
#            w = float(box[2] - box[0] + 1)
           # h = float(box[3] - box[1] + 1)
            h= float(box[3])
            cls = yolov3_cls_to_ssd[cls]
           # print (image_id)
           # print (cls)
           # with open('/home/rijurekha/Trafficdata/listold.txt','r') as fp:
            #    for line in fp:
             #      line = fp.readline()
              #     base=os.path.basename(line)
        #print("This is base")
         # print(base)
               #    str=os.path.splitext(base)[0]
         # print("This is string file")
         # print (str)
          #print (image_id)
#                   print("We are findin string")
 #                  print(str)
  #                 print(image_id)
                #   if(str==image_id):
            results.append({'image_id': image_id,
                            'category_id': int(cls),
                            'bbox': [x, y, w, h],
                            'score': float(conf)})
    #print(len(results))  
    with open(results_file, 'w') as f:
      #with open('/home/rijurekha/Trafficdata/listnew.txt','r') as fp:
       #   line = fp.readline()
        #  base=os.path.basename(line)
         # print("This is base")
         # print(base)
         # str=os.path.splitext(base)[0]
         # print("This is string file")
         # print (str)
         # print (image_id)
         # if(str==image_id):
          #    print ("yes dear")
         f.write(json.dumps(results, indent=4))


def main():
    args = parse_args()
    check_args(args)

    results_file = 'trafficyolofp16_results.json'
    yolo_dim = int(args.model.split('-')[-1])  # 416 or 608
    trt_yolov3 = TrtYOLOv3(args.model, (yolo_dim, yolo_dim))

    jpgs = [j for j in os.listdir(args.imgs_dir) if j.endswith('.jpg')]
    generate_results(trt_yolov3, args.imgs_dir, jpgs, results_file)

    # Run COCO mAP evaluation
    # Reference: https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoEvalDemo.ipynb
    YOUR_CAT_IDS = [1]
    cocoGt = COCO(args.annotations)
    #imgIds= sorted(cocoGt.getImgIds())
    cocoDt = cocoGt.loadRes(results_file)
    imgIds = sorted(cocoGt.getImgIds())
    cocoEval = COCOeval(cocoGt, cocoDt, 'bbox')
    cocoEval.params.imgIds = imgIds
    cocoEval.params.catIds = YOUR_CAT_IDS 
    cocoEval.evaluate()
    cocoEval.accumulate()
    print(cocoEval.summarize())


if __name__ == '__main__':
    main()
