# Image Metadata Remover

A simple Streamlit web app to remove metadata (such as EXIF data) from images. Users can upload JPG, JPEG, or PNG images, and download a clean version with all metadata stripped.

## Features

- Upload images in JPG, JPEG, or PNG formats
- Remove all metadata while preserving the image pixels
- Preview the cleaned image in the browser
- Download the metadata-free image as a JPEG file

## How it Works

The app uses the Python Pillow (PIL) library to open the uploaded image and extract just the pixel data. A new image is created with this pixel data only, discarding all embedded metadata like EXIF. This new image can then be downloaded without any metadata.

## Installation

1. Clone this repository or copy the source code.
2. Make sure you have Python 3 installed.
3. Install dependencies:

```

pip install streamlit pillow

```

## Running the App

To start the Streamlit app, run:

```

streamlit run app.py

```

Replace `app.py` with the filename of the source code.

## Usage

1. Open the app in your browser (usually at `http://localhost:8501`).
2. Click "Upload an image" and select a JPG, JPEG, or PNG file.
3. View the image displayed without metadata.
4. Click "Download Metadata-free Image" to save the cleaned image locally.

## Limitations and Notes

- The cleaned image is saved as a JPEG file regardless of original format.
- Transparency in PNG files will be lost when converted to JPEG.
- The app removes metadata by rebuilding the image pixel data only.
- For advanced metadata removal, consider specialized tools.

## License

This project is open source under the MIT License.

```
