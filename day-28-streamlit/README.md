# Day 28 - Streamlit Interactive Dashboard

A simple, interactive dashboard created using Streamlit to visualize sample data with minimal code.  
Perfect for quick prototyping and exploring data visually without complex setup.

## Features

- Displays a table of numbers and their squared and cubed values.
- Interactive slider to multiply numbers dynamically and update the display.
- Line chart that visualizes number, squared, and cubed values.
- Built entirely in Python, no HTML/CSS required.

## Installation

1. Clone this repo or download the code.
2. Install the required packages:
```

pip install streamlit pandas numpy

```

## Usage

Run the Streamlit app with this command:
```

python -m streamlit run day28_dashboard.py

```

This will open a local web page where you can interact with the slider and see the changes live.

## Code Overview

- `streamlitdashboard.py` contains all the code.
- Uses `streamlit` for the UI, `pandas` for data handling, and `numpy` for numeric calculations.
- Shows how easy it is to create interactive data apps quickly using Streamlit.
