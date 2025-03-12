import os
import glob
import pandas as pd

# ----- Set your folder paths here -----
input_folder = '/Users/bklink/Desktop/CSVProcessing/input_html_files'
output_folder = '/Users/bklink/Desktop/CSVProcessing/output_csv_files'
os.makedirs(output_folder, exist_ok=True)

def process_file(text_file):
    """
    Processes a file containing sensor data lines (CSV-like),
    even if the file has a misleading .html extension.
    """
    print(f"\nProcessing {text_file}...")
    with open(text_file, "r", encoding="utf-8") as f:
        lines = f.read().strip().splitlines()

    records = []
    for line in lines:
        line = line.strip()
        if not line or len(line.split(",")) < 12:
            continue

        try:
            import re
            match = re.match(r"(.+?Z)(\d*),(.*)", line)
            if match:
                timestamp = match.group(1)
                sensor_id = match.group(2)
                rest = match.group(3).split(",")
                fields = [timestamp, sensor_id] + rest
            else:
                fields = line.split(",")

            if len(fields) not in [14, 15]:  # 14 = old format, 15 = newer with epoch
                print(f"Skipping malformed line: {line}")
                continue

            records.append(fields)
        except Exception as e:
            print(f"Error parsing line: {line}. Error: {e}")
            continue

    if not records:
        print(f"No valid records found in {text_file}.")
        return None

    if len(records[0]) == 15:
        columns = [
            "Timestamp",
            "Sensor_ID",
            "Message_Length",
            "Sense_Timestamp",
            "Serial_ID",
            "Temperature_C",
            "Humidity_%",
            "Gas_Resistance_1_KOhm",
            "Gas_Resistance_2_KOhm",
            "Gas_Resistance_3_KOhm",
            "Gas_Resistance_4_KOhm",
            "Altitude_m",
            "Battery_Voltage_V",
            "RSSI_dBm",
            "SNR_dB",
        ]
    else:
        columns = [
            "Timestamp",
            "Sensor_ID",
            "Message_Length",
            "Serial_ID",
            "Temperature_C",
            "Humidity_%",
            "Gas_Resistance_1_KOhm",
            "Gas_Resistance_2_KOhm",
            "Gas_Resistance_3_KOhm",
            "Gas_Resistance_4_KOhm",
            "Altitude_m",
            "Battery_Voltage_V",
            "RSSI_dBm",
            "SNR_dB",
        ]

    df = pd.DataFrame(records, columns=columns)
    print(f"Extracted {len(df)} valid records from {text_file}.")
    return df

def convert_and_save(df, text_file):
    """
    Converts DataFrame columns to appropriate types and saves as a CSV file in the output folder.
    """
    expected_columns = {
        "Timestamp": str,
        "Sensor_ID": int,
        "Message_Length": int,
        "Sense_Timestamp": int,
        "Serial_ID": str,
        "Temperature_C": float,
        "Humidity_%": float,
        "Gas_Resistance_1_KOhm": float,
        "Gas_Resistance_2_KOhm": float,
        "Gas_Resistance_3_KOhm": float,
        "Gas_Resistance_4_KOhm": float,
        "Altitude_m": float,
        "Battery_Voltage_V": float,
        "RSSI_dBm": int,
        "SNR_dB": int,
    }

    available_columns = [col for col in expected_columns if col in df.columns]
    df = df[available_columns]

    for col in available_columns:
        try:
            df[col] = df[col].astype(expected_columns[col])
        except Exception as e:
            print(f"Error converting column '{col}' in file {text_file}: {e}")

    base_name = os.path.splitext(os.path.basename(text_file))[0]
    csv_file = os.path.join(output_folder, base_name + ".csv")
    df.to_csv(csv_file, index=False)
    print(f"✅ Saved CSV to {csv_file}")

# ---- Main Execution ----
files = glob.glob(os.path.join(input_folder, "*.html"))  # still looking for .html extension
if not files:
    print("No .html files found in the input folder.")
else:
    for file in files:
        df = process_file(file)
        if df is not None and not df.empty:
            convert_and_save(df, file)
