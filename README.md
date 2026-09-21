# Defect Detector — HackALEM Rehearsal

Simple computer vision solution for the Track 02 task.

The program receives an image and classifies it as:

- `OK`
- `DEFECT`

## How it works

The solution uses OpenCV.

The image is converted to HSV color space and the program calculates how much of the image contains red regions.

If more than 10% of the image is red, the image is classified as:

`DEFECT`

Otherwise:

`OK`

This is a simple rule-based CV approach and does not require a trained ML model.

## Installation

```bash
pip install -r requirements.txt
