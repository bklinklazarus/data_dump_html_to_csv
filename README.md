# data_dump_html_to_csv

## Overview

`data_dump_html_to_csv` is a Python script designed to process sensor data files with an HTML extension that contain CSV-like content. The script reads each file from a designated input folder, parses and cleans the data, converts it into a structured Pandas DataFrame with appropriate data types, and saves the cleaned data as CSV files in an output folder. It handles multiple data formats and includes error logging for malformed rows.

## Features

- **HTML Parsing:** Strips extraneous HTML tags and extracts CSV data.
- **Data Transformation:** Supports two sensor data formats (old and new) with field conversions.
- **Error Handling:** Skips malformed lines and logs parsing errors.
- **Output Conversion:** Saves the processed data as CSV files for easy integration with downstream processes.

## Prerequisites

- Python 3.6 or higher
- Required Python libraries:
  - `pandas`
  - `glob`
  - `os`
  - `re`

Install the necessary package using pip:

```bash
pip install pandas

## Setup

### Input/Output Folders:
- Set the `input_folder` variable to the directory containing your HTML sensor data files.
- Set the `output_folder` variable to the directory where you want the converted CSV files to be saved.

### Script Configuration:
- Adjust any configuration parameters as needed (e.g., file paths, column data types) directly in the script.

## Usage

Run the script using Python:

```bash
python data_dump_html_to_csv.py

The script will:
- Search for `.html` files in the input folder.
- Process each file by parsing and cleaning the sensor data.
- Convert the cleaned data into a Pandas DataFrame with proper types.
- Save the resulting data as CSV files in the output folder.

Error Handling:
- The script skips lines that are malformed (e.g., those with an unexpected number of columns) and logs these occurrences.
- Conversion errors are caught and printed, ensuring that the script continues processing other rows/files.
