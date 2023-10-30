# CV-people-counter

This is a computer vision-based people counter system.

## About

The purpose of this project is to develop a people counter system that uses computer vision technology to accurately count the number of people entering and exiting a building or specific area.

The system uses a camera to capture video footage and apply object detection and tracking algorithm (centroid tracker) to detect and count people.

The system provides real-time data on the number of people in the area.

## Hardware Requirements

- Camera
- Computer (Server with GPU)

## Software Requirements

- Python
- Visual Studio Code
- OpenCV, NumPy, SciPy, MobileNet SSD

## Installation

> [!NOTE]
> Ensure that you have supported version `Python 3.11.3` and `pip` installed on your system.
<br />

To begin, install all the necessary Python dependencies by executing the following command:

```
pip install -r requirements.txt
```
<br />
 
To run inference on a test video file, navigate to the root directory of the project and run the following command:

```
python cv-people-counter.py --prototxt detector/MobileNetSSD_deploy.prototxt --model detector/MobileNetSSD_deploy.caffemodel --input utils/test_1.mp4
```
<br />

To run inference on a webcam, set `"url": 0` in `utils/config.json` and run the following command:

```
python cv-people-counter.py --prototxt detector/MobileNetSSD_deploy.prototxt --model detector/MobileNetSSD_deploy.caffemodel
```

## Usage

For help and to see other arguments, `--help` or `-h`:

```
python cv-people-counter.py --help
```

