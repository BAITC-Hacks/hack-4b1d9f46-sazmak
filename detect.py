import sys
import cv2
import numpy as np

def detect_defect(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Cannot open image: {image_path}")

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Red color has two ranges in HSV
    lower_red_1 = np.array([0, 100, 100])
    upper_red_1 = np.array([10, 255, 255])

    lower_red_2 = np.array([170, 100, 100])
    upper_red_2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red_1, upper_red_1)
    mask2 = cv2.inRange(hsv, lower_red_2, upper_red_2)

    red_mask = mask1 + mask2

    red_pixels = np.count_nonzero(red_mask)
    total_pixels = image.shape[0] * image.shape[1]

    red_ratio = red_pixels / total_pixels

    threshold = 0.10

    if red_ratio > threshold:
        result = "DEFECT"
    else:
        result = "OK"

    print(f"Result: {result}")
    print(f"Red area: {red_ratio * 100:.2f}%")

    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python detect.py <image>")
        sys.exit(1)

    detect_defect(sys.argv[1])
