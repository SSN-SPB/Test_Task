# Purpose of script
This script is designed to generate mask screenshot for image. <br>
## Case
There is initial image that contains areas that should be ignored during UI screenshot comparison test
## Flow
- Create copy of this image and paint(hide) areas that should be ignored during UI screenshot comparison test
- Run the script to save the difference between these two files to separate mask image
## Result
The mask image is generated



# Using the script
## Prerequisites
The script requires Python 3.x and the following libraries:
```commandline
from PIL import Image
```
## Data Preparation
### 1. Prepare Initial Image 
The image should be in a format supported by the PIL library, such as JPEG or PNG.<br>
In the script it is named as "actual_screenshot.png" <br>
### 2. Prepare copy of the initial image with applied mask
The image should be in a format supported by the PIL library, such as JPEG or PNG.<br>
In the script it is named as "actual_screenshot_with_added_mask.png"
### 3. Copy these images to the same directory
Images should be placed in the same directory with the script<br>
## Running the script
To run the script, execute the following command in your terminal:
```
python generate_mask.py
```
Or by clicking the "Run" button in your IDE if you are using one. <br>

# The expected result
The script will generate a mask image named "created_mask_image.png" in the same directory as the script. <br>

# Using resulting image
## A. As mask for further processing
The resulting mask image can be used for further processing, <br>
e.g. as 'mask image' in automation tests to apply it to referenced and actual screenshots to mask areas
that should be ignored in the comparison - e.g. daily/user data. <br>
## B. For manual checking the difference between two screenshots
The result is a visualization of differences between initial and tested screenshots that are received
during automation tests<br>


