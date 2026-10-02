# Purpose of script
This script is designed to generate masks for images using a specified algorithm. <br>
It can be used in various applications such as image processing, computer vision, <br>
and machine learning tasks where masking is required. <br>

# Runnin the script
## Prerequisites
The script requires Python 3.x and the following libraries:
```commandline
from PIL import Image
```
## Data Preparation
### 1. Prepare Initial Image 
The image should be in a format supported by the PIL library, such as JPEG or PNG.<br>
In the script it is named as "actual_screenshot.png" and should be placed in the same directory as the script. <br>
### 2. Prepare copy of the initial image with applied mask
The image should be in a format supported by the PIL library, such as JPEG or PNG.<br>
In the script it is named as "actual_screenshot_with_added_mask.png"
It should be placed in the same directory as the script as well <br>
## Running the script
To run the script, execute the following command in your terminal:
```
python mask_generating_script.py
```
Or by clicking the "Run" button in your IDE if you are using one. <br>

# The expected result
The script will generate a mask image named "found_difference_mask_image.png" in the same directory as the script. <br>

# Using resulting mask image
## A. As mask for further processing
The resulting mask image can be used for further processing, <br>
e.g. as 'mask image' in automation tests to apply it to initial and tested screenshots to mask areas
that should be ignored in the comparison. <br>
## B. As a final result 
The result is a visualization of differences between initial and tested screenshots that are received
during automation tests or during manual testing.<br>


