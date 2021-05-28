# yolo_example

A simple example to test pretrained YOLO object detection model on a single image.

[Check Load YOLOv5 from PyTorch Hub](https://github.com/ultralytics/yolov5/issues/36)

To run the model, first create a conda environment: 
> $ conda create -n myenv python=3.8

then activte the environment:
> conda activate myenv

To install the requirements in a conda environment in **Python>=3.8**:

> $ pip install -r https://raw.githubusercontent.com/ultralytics/yolov5/master/requirements.txt





To run on a single image:
> $ python yolo_test.py img_file_name

The results showing the bounding boxes drawn for the detected objects will be saved under runs/hub folder.
