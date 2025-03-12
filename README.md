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
