# AccuracyRT_Darknet


# Steps to obtain the accuracy using TensorRT
1. TensorRT engine creation
2. Accuracy calculation

# Software Requirements 
1. TensorRT ( version preferably >= 5)
2. ONNX (sudo pip3 install onnx==1.4.1)
3. Pycotools(Used to calculate the MAP)


# Steps to create the TensorRT engine
1. Go to <i>cd tensorrt_accuracy/yolo </i>
2. Generate the onnx model from the weights and the cfg file( python3 yolo_to_onnx.py)
3. After the onnx is generated, run <i> python3 onnx_to_tensorrt.py --m yolov3-tiny-416</i>(The type of model can be changed inside the onnx_to_tensorrt.py file)
4. This will generate the model with trt extension.


# Accuracy Calculation

1. Open eval_yolo.py inside the directory tensorrt_accuracy
2. Give the path to the image dataset along with the annotations in json format(format attached in the folder)
3. Run python3 eval_yolo.py --m <model> (Here model is either tiny-yolo or yolo. Give the name of the trt engine generated above)
4. This will go through all the images and the annotations and will generate a file with the format .json. After it, the COCOeval of pycocotools will evaluate the json file and generate the summary of the results(Both precison and recall). The dummy screenshot of the output is attached.
  ![alt text](http://url/to/img.png)
5. Note that in order to get the precision and recall for individual classes, you need to specify the class in the code (Line no 120 of eval_yolo.py)
  
