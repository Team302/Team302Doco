Training YOLOv8 Models for Hailo-8
===================================

This guide covers the complete workflow for training a YOLOv8 object detection model on a Linux machine with GPU acceleration and compiling it to run on a Hailo-8 AI accelerator.

Prerequisites
-------------

Hardware Requirements
^^^^^^^^^^^^^^^^^^^^^

* Linux machine with NVIDIA GPU (for training)
* A large amount of VRAM may be required for training large models(e.g. 4-6 GB for yolov8n, 10-11 GB for yolov8m)
* Hailo-8 device (for deployment)
* Minimum 16GB RAM (32GB+ recommended for training)
* 75GB+ free disk space

Software Requirements
^^^^^^^^^^^^^^^^^^^^^

* Ubuntu 20.04 or 22.04 (recommended)
* NVIDIA drivers installed
* Docker with NVIDIA Container Toolkit
* Python 3.8 or higher
* CUDA 11.0+ and cuDNN

Part 1: Setting Up the Training Environment
--------------------------------------------

Install NVIDIA Drivers and CUDA
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Check if NVIDIA drivers are installed
   nvidia-smi
   
   # Install NVIDIA drivers if needed (Ubuntu)
   sudo apt update
   sudo apt install nvidia-driver-525
   sudo reboot

Install Docker and NVIDIA Container Toolkit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   
   # Install NVIDIA Container Toolkit
   distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
   curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
   curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | \
     sudo tee /etc/apt/sources.list.d/nvidia-docker.list
   
   sudo apt-get update
   sudo apt-get install -y nvidia-container-toolkit
   sudo systemctl restart docker
   
   # Test NVIDIA Docker
   docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi

Install Python and YOLOv8
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Create a virtual environment
   python3 -m venv yolov8-env
   source yolov8-env/bin/activate
   
   # Install Ultralytics YOLOv8
   pip install ultralytics
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

Part 2: Preparing Your Dataset
-------------------------------

ROBOFLOW
^^^^^^^^

You can use Roboflow to easily create and manage your dataset:

1. Sign up at https://roboflow.com/
2. Upload your images and annotate them
3. Export the dataset in YOLO format

the exported data is in the following format:
Dataset Structure
^^^^^^^^^^^^^^^^^

YOLOv8 expects datasets in YOLO format with the following structure:

.. code-block:: text

   dataset/
   ├── images/
   │   ├── train/
   │   │   ├── image1.jpg
   │   │   ├── image2.jpg
   │   │   └── ...
   │   └── val/
   │       ├── image1.jpg
   │       └── ...
   └── labels/
       ├── train/
       │   ├── image1.txt
       │   ├── image2.txt
       │   └── ...
       └── val/
           ├── image1.txt
           └── ...

Label Format
^^^^^^^^^^^^

Each label file contains one line per object in YOLO format:

.. code-block:: text

   class_id center_x center_y width height

Where all coordinates are normalized to [0, 1]:

* ``class_id``: Integer class index (starting from 0)
* ``center_x``: X coordinate of bounding box center
* ``center_y``: Y coordinate of bounding box center
* ``width``: Width of bounding box
* ``height``: Height of bounding box

Create Dataset Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a ``dataset.yaml`` file:

.. code-block:: yaml

   # dataset.yaml
   path: /path/to/dataset
   train: images/train
   val: images/val
   
   # Number of classes
   nc: 3
   
   # Class names
   names:
     0: class1
     1: class2
     2: class3

Part 3: Training YOLOv8 Model
------------------------------

Basic Training
^^^^^^^^^^^^^^

.. code-block:: bash

   # Activate environment
   source yolov8-env/bin/activate
   
   # Train YOLOv8n (nano) model
   yolo detect train data=dataset.yaml model=yolov8n.pt epochs=100 imgsz=640 batch=16

Training Parameters
^^^^^^^^^^^^^^^^^^^

Key training parameters:

* ``model``: Pre-trained model (yolov8n.pt, yolov8s.pt, yolov8m.pt, yolov8l.pt, yolov8x.pt)
* ``epochs``: Number of training epochs (typically 100-300)
* ``imgsz``: Image size (640 is standard, must be multiple of 32)
* ``batch``: Batch size (adjust based on GPU memory)
* ``device``: GPU device (0, 1, or cpu)

Training metrics are saved to ``runs/detect/train_exp/``. View with TensorBoard:

---------------------------------

Export to ONNX Format
^^^^^^^^^^^^^^^^^^^^^

Hailo requires models in ONNX format first:

.. code-block:: bash

   # Export best model to ONNX
   yolo export model=runs/detect/train_exp/weights/best.pt format=onnx imgsz=640 simplify=True

Or with Python:

.. code-block:: python

   from ultralytics import YOLO
   
   # Load trained model
   model = YOLO('runs/detect/train_exp/weights/best.pt')
   
   # Export to ONNX
   model.export(
       format='onnx',
       imgsz=640,
       simplify=True,
       opset=11,
   )

This creates ``best.onnx`` in the same directory.

Part 5: Compile Model with Hailo Docker
----------------------------------------

Pull Hailo Docker Image
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Pull the Hailo Dataflow Compiler Docker image
   docker pull hailo/hailo_ai_sw_suite:2023-07
   
   # Verify the image
   docker images | grep hailo

Start Hailo Docker Container
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Create a working directory
   mkdir -p ~/hailo-workspace
   cd ~/hailo-workspace
   
   # Copy your ONNX model
   cp /path/to/best.onnx ~/hailo-workspace/
   
   # Run Hailo container with GPU support
   docker run -it --gpus all \
     -v ~/hailo-workspace:/workspace \
     --name hailo-compiler \
     hailo/hailo_ai_sw_suite:2023-07 \
     /bin/bash

Compile Model to HEF Format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Inside the Docker container, use the Hailo Dataflow Compiler:

.. code-block:: bash

   # Navigate to workspace
   cd /workspace
   
   # Compile ONNX model to HEF (Hailo Executable Format)
   hailomz compile yolov8n \
     --ckpt best.onnx \
     --hw-arch hailo8 \
     --calib-path /path/to/calibration/images \
     --classes 2 \
     --performance \
     --output-dir ./compiled

Calibration Dataset
^^^^^^^^^^^^^^^^^^^

The calibration process needs representative images:

There are some scripts on github that automate the process
.. code-block:: bash

   # Create calibration directory with 50-100 representative images
   mkdir -p ~/hailo-workspace/calibration_images
   
   # Copy representative images from your validation set
   cp dataset/images/val/*.jpg ~/hailo-workspace/calibration_images/


Part 6: Deploy to Hailo-8 Device
---------------------------------

Copy HEF to Target System
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   # Exit Docker container
   exit
   
   # HEF file is now in ~/hailo-workspace/
   ls ~/hailo-workspace/*.hef
   
   # Copy to your robot or target device
   scp ~/hailo-workspace/yolov8n_hailo8.hef user@robot:/path/to/models/

Python Inference Code
^^^^^^^^^^^^^^^^^^^^^^

Example Python code for inference on Hailo-8:

.. code-block:: python

   from hailo_platform import (
       HEF, Device, VDevice, HailoStreamInterface, 
       InferVStreams, ConfigureParams
   )
   import numpy as np
   import cv2
   
   class YOLOv8Hailo:
       def __init__(self, hef_path):
           self.hef = HEF(hef_path)
           self.device = Device()
           self.network_group = self.device.configure(self.hef)[0]
           
       def preprocess(self, image):
           """Preprocess image for YOLOv8"""
           # Resize to model input size
           img = cv2.resize(image, (640, 640))
           # Convert BGR to RGB
           img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
           # Normalize to [0, 1]
           img = img.astype(np.float32) / 255.0
           # Add batch dimension
           img = np.expand_dims(img, axis=0)
           return img
       
       def postprocess(self, outputs, conf_threshold=0.25):
           """Post-process YOLOv8 outputs"""
           # Implementation depends on your specific model output format
           # Typically involves:
           # 1. Decoding bounding boxes
           # 2. Applying confidence threshold
           # 3. Non-maximum suppression
           detections = []
           # Your post-processing logic here
           return detections
       
       def infer(self, image):
           """Run inference on image"""
           # Preprocess
           input_data = self.preprocess(image)
           
           # Run inference
           with InferVStreams(self.network_group) as infer_pipeline:
               input_dict = {self.hef.get_input_vstream_infos()[0].name: input_data}
               output_dict = infer_pipeline.infer(input_dict)
           
           # Post-process
           detections = self.postprocess(output_dict)
           return detections
   
   # Usage
   detector = YOLOv8Hailo('yolov8n_hailo8.hef')
   image = cv2.imread('test_image.jpg')
   results = detector.infer(image)

Best Practices
--------------

Training Tips
^^^^^^^^^^^^^

1. **Use transfer learning**: Always start with pre-trained weights
2. **Augmentation**: Enable data augmentation for better generalization
3. **Dataset size**: Aim for at least 1500+ images per class
4. **Class balance**: Try to balance the number of samples per class
5. **Image quality**: Use high-quality, representative images
6. **Validation split**: Use 80/20 or 70/30 train/val split

Hailo Optimization Tips
^^^^^^^^^^^^^^^^^^^^^^^

1. **Model size**: Smaller models (YOLOv8n, YOLOv8s) compile faster and run better on Hailo-8
2. **Input size**: 640x640 is standard, but 416x416 may be faster
3. **Calibration data**: Use 50-100 diverse, representative images
4. **Compression**: Higher compression saves memory but may reduce accuracy
5. **Testing**: Always validate HEF accuracy against original model

Troubleshooting
---------------

Training Issues
^^^^^^^^^^^^^^^

**Out of memory during training**:

.. code-block:: bash

   # Reduce batch size
   yolo detect train data=dataset.yaml model=yolov8n.pt batch=8
   
   # Or use smaller model
   yolo detect train data=dataset.yaml model=yolov8n.pt

**Poor training results**:

* Check dataset labels are correct
* Increase epochs (300-500 for small datasets)
* Adjust learning rate
* Use more data augmentation

Compilation Issues
^^^^^^^^^^^^^^^^^^

**ONNX export fails**:

.. code-block:: bash

   # Try different opset version
   yolo export model=best.pt format=onnx opset=11 simplify=True

**HEF compilation fails**:

* Ensure ONNX model is simplified
* Check calibration images are valid
* Try lower compression level
* Verify model architecture is supported by Hailo

Performance Issues
^^^^^^^^^^^^^^^^^^

**Slow inference on Hailo-8**:

* Use smaller input size (416 instead of 640)
* Choose lighter model (yolov8n instead of yolov8s)
* Enable hardware optimizations during compilation

**Accuracy drop after compilation**:

* Use more calibration images
* Lower compression level
* Verify post-processing implementation

Additional Resources
--------------------

* `Ultralytics YOLOv8 Documentation <https://docs.ultralytics.com/>`_
* `Hailo Developer Zone <https://hailo.ai/developer-zone/>`_
* `Hailo Model Zoo <https://github.com/hailo-ai/hailo_model_zoo>`_
* `YOLO Dataset Format <https://docs.ultralytics.com/datasets/detect/>`_

Example Workflow Summary
------------------------

Complete workflow from start to finish:

.. code-block:: bash

   # 1. Prepare environment
   source yolov8-env/bin/activate
   
   # 2. Train model
   yolo detect train data=dataset.yaml model=yolov8n.pt epochs=100 imgsz=640 batch=16
   
   # 3. Validate model
   yolo detect val model=runs/detect/train/weights/best.pt data=dataset.yaml
   
   # 4. Export to ONNX
   yolo export model=runs/detect/train/weights/best.pt format=onnx imgsz=640 simplify=True
   
   # 5. Start Hailo Docker
   docker run -it --gpus all -v ~/hailo-workspace:/workspace hailo/hailo_ai_sw_suite:2023-07 /bin/bash
   
   # 6. Inside Docker: Compile to HEF
   hailo parser onnx /workspace/best.onnx
   hailo optimize --model-name yolov8n --hw-arch hailo8 --calib-set /workspace/calibration_images
   hailo compiler --hw-arch hailo8 yolov8n_optimized.har --output yolov8n_hailo8.hef

This completes the full pipeline from training to deployment on Hailo-8 hardware.