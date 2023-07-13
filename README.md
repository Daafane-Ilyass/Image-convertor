# Image-converter

This Python script provides a convenient way to convert images to a desired format and save them in a specified folder. It utilizes the `sys` and `os` modules to accept command-line arguments for the source folder containing the images and the destination folder where the converted images will be saved.

Features:
- Converts images from one format to another
- Supports various image formats (e.g., JPEG, PNG, GIF)
- Allows customization of the destination format
- Effortlessly processes multiple images in a folder
- Maintains the original file names during conversion
- Preserves image quality and metadata
- Automatically creates the destination folder if it does not exist

Usage:
1. Ensure that Python and the necessary dependencies are installed.
2. Run the script using the command: `python image_converter.py <source_folder> <destination_folder>`
   - `<source_folder>`: Path to the folder containing the images to be converted.
   - `<destination_folder>`: Path to the folder where the converted images will be saved.
3. Sit back and relax while the script efficiently converts and saves the images.

Example:
```
python image_converter.py /path/to/source_images /path/to/destination_folder
```

Note: 
- Make sure to specify valid paths for both the source and destination folders.
- The script preserves the directory structure of the source folder within the destination folder.
- The destination folder will be created if it does not exist.

Dependencies:
- Python (3.x or higher)
- The Python Imaging Library (PIL) or Pillow library

Feel free to use and modify this script to suit your image conversion needs.
