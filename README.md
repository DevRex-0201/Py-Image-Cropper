# Image Cropping Processor

## Overview
This Python script provides a simple GUI-based image processing tool using the Tkinter library. The script allows users to specify a folder containing images and apply processing operations such as cropping and resizing to each image in the folder. The processed images are then saved with a specified result file prefix.

## Dependencies
Ensure that you have the following libraries installed before running the script:

- `os`: Operating system interface (usually included in Python standard library)
- `tkinter`: GUI toolkit for Python
- `PIL` (Python Imaging Library, also known as Pillow): Image processing library

You can install Pillow using the following command:
```bash
pip install Pillow
```

## How to Use

### 1. Run the Script
Execute the script in a Python environment.

```bash
python image_processor.py
```

### 2. GUI Interface

#### Folder Path
- Use the "Browse" button to select the folder containing the images you want to process.

#### Result File Prefix
- Specify the prefix that will be added to the filenames of the processed images.

#### Cropped Height
- Enter the height (in pixels) to be cropped from the bottom of each image.

#### Image Count (Optional)
- Optionally, specify the number of images to process. If left blank, all images in the folder will be processed.

#### Process Images
- Click the "Process Images" button to start the image processing.

### 3. Image Processing
- The script processes each image in the selected folder.
- It crops the specified height from the bottom of each image.
- It resizes the images to a new height (800 pixels) while maintaining the aspect ratio.
- Processed images are saved in the "output/" folder with filenames prefixed by the specified result file prefix.

### 4. Success Message
- After processing is complete, a success message will be displayed.

## Notes
- Supported image formats: PNG, JPG, JPEG, GIF.
- The script uses Tkinter for the graphical interface, and Pillow for image processing.

Feel free to customize the script for your specific use case or modify the processing operations as needed.
