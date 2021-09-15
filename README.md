
# Steps to obtain the accuracy for TensorRT engines
1. TensorRT engine creation
2. Accuracy calculation

# Software Requirements 
<b> 1. TensorRT (version preferably >= 5) </b> <br>
<b> 2. ONNX (sudo pip3 install onnx==1.4.1)---> The present yolo_to_onnx.py works only with version 1.4.1 of ONNX </b> <br>
<b> 3. Pycotools (Used to calculate the MAP) </b> <br>
<b> 4. Tested on Ubuntu 18.04 </b> <br>

# Steps to create the TensorRT engine
1. Go to <i>cd tensorrt_accuracy/yolo </i>
2. Generate the onnx model from the weights and the cfg file( <i>python3 yolo_to_onnx.py</i>)
3. After the onnx is generated, run <i> python3 onnx_to_tensorrt.py --m yolov3-tiny-416</i>(The type of model can be changed inside the onnx_to_tensorrt.py file)
4. This will generate the model with trt extension.


# Accuracy Calculation

1. Open eval_yolo.py inside the directory tensorrt_accuracy
2. Give the path to the image dataset along with the annotations in json format(format attached in the folder)
3. Run <i>python3 eval_yolo.py --m model</i> (Here model is either tiny-yolo or yolo. Give the name of the trt engine generated above)
4. This will go through all the images and the annotations and will generate a file with the format .json. After it, the COCOeval of pycocotools will evaluate the json file and generate the summary of the results(Both precison and recall). The dummy screenshot of the output is attached
 ![Accuracy_output](mdoutput.png)
5. Note that in order to get the precision and recall for individual classes, you need to specify the class in the code (<b>Line no 120 of eval_yolo.py</b>). This is the link to the code(https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py)

# Additional Changes needed:
To obtain precision and recall at some fixed IOU(say 0.75), you can edit the <b>cocoeval.py</b> (Edit function Summarize in the file) file present in the system as pycocotools is installed. <i>cocoeval.py</i> is present at the location <i> ~/coco/PythonAPI/pycocotools/cocoeval.py</i> (Assuming the pycocotools is installed in the home directory)


# Steps to obtain the accuracy for Darknet Models
1. <i> cd darknet </i>
2. <i> make -j 4 </i> ( This will build all the necessary files)
3. Do a basic test whether darknet is working fine. <i>./darknet detect yolov3-tiny-416.cfg yolov3-tiny-416.weights data/dog.jpg </i> 
 ![Darknet_sample](darknetsampleout.png)

# Command to obtain recall 
---->  <i> ./darknet detector recall cfg/voc.data cfg/yolov3-tiny-416.cfg yolov3-tiny-416.weights </i> (voc.data contains the paths to the training and the test dataset)


# Command to obtain MAP
----> <i> ./darknet detector map cfg/voc.data cfg/yolov3-tiny-416.cfg yolov3-tiny-416.weights </i> 



  
