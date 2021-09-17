
# Accuracy Calculation
1. Open eval_yolov3.py inside the directory tensorrt_accuracy. <br>
2. Give the path to the image dataset along with the annotations in json format(file attached in the folder).<br>
3. Run <i>python3 eval_yolov3.py --m model</i> (Here model is either tiny-yolo or yolo. Give the name of the trt engine generated above).<br>
4. This will go through all the images and the annotations and will generate a file with the format .json. After it, the COCOeval of pycocotools will evaluate the json file and generate the summary of the results (Both precison and recall). The dummy screenshot of the output is attached.
 ![Accuracy_output](mdoutput.png)
 5. Note that in order to get the precision and recall for individual classes, you need to specify the class in the code (<b>Line no 120 of eval_yolo.py</b>). This is the link to the code(https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/cocoeval.py)<br>

<h3> Additional Changes needed</h3>
 To obtain precision and recall at some fixed IOU(say 0.75), you can edit the <b>cocoeval.py</b> (Edit function Summarize in the file) file present in the system as pycocotools is installed. <i>cocoeval.py</i> is present at the location <i> ~/coco/PythonAPI/pycocotools/cocoeval.py</i> (Assuming the pycocotools is installed in the home directory)


# Steps to obtain the accuracy for Darknet Models

<h3> Command to obtain recall</h3>
 ./darknet detector recall fig3.data yolov3-tiny-416.cfg yolov3-tiny-416.weights (fig3.data contains the paths to the training and the test dataset which can be downloaded from the google drive link given)
 <br>
 <b>Note:</b><i> All the above files are present in the folder "Indian-Traffic-Dataset". Give the path of this folder when the darknet is to be run.</i>


<h3> Command to obtain MAP </h3>
./darknet detector map fig3.data yolov3-tiny-416.cfg yolov3-tiny-416.weights 


# Dataset used in our evaluation
We use our custom traffic dataset for the evaluation. It can be found at https://drive.google.com/drive/folders/1AktwXwKcyJZnHcaFMl2jau92jIz8X9fo?usp=sharing

# Contact
For any issues related to the code, you can contact me at <i>omais.shafi@gmail.com</i>
  
