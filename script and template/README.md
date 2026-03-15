# SmallAlley-LinkNet

A set of Python scripts designed to automate and standardize the CSV to KML conversion process for the **LinkNet SMALL ALLEY** project. 

## ⚠️ Project Status & Disclaimer
**Last Updated: December 23, 2025**

This code still has many possibilities for improvement and optimization, but right now I have no time to continue developing this specific local project. 

Because LinkNet's standards and requirements for this project may change over time, I intentionally separated the code based on the placemark type (Pole, FAT, Homepass, Clamp Hook). This modular approach ensures that if a styling standard changes for one element, you only need to update that specific script without breaking the rest of the pipeline.

## ✨ Features & KML Styling Applied

These scripts take raw CSV data and convert them into standard Google Earth KML files with specific, automated styling based on LinkNet's requirements:

* **FAT (Fiber Access Terminal) Converter (`convert_fat_to_kml.py`)**
    * Dynamically styles points based on the length of the `FAT ID/NETWORK ID`.
    * **Normal Length:** Styled as a Green Triangle (scaled up).
    * **Short Length (< 9 chars):** Styled as a White Square (scaled down) to easily spot anomalies or specific FAT types.
* **HP (Homepass) Converter (`convert_hp_to_kml.py`)**
    * Automatically categorizes and separates data into two distinct KML folders: `HOME` (for RESIDENCE) and `HOME-BIZ` (for non-RESIDENCE).
    * Applies conditional icon styling based on the business category and whether the homepass requires a Clamp Hook.
* **Pole Converter (`convert_pole_to_kml.py`)**
    * Generates Pole KMLs with detailed, formatted pop-up balloons (Pole ID, Coordinates, Provider, Type, LINE).
    * Uses standardized Google Maps icons for highlighted and normal states.
* **Clamp Hook (CH) Converter (`convert_ch_to_kml.py`)**
    * Standardizes Clamp/Hook coordinates into a specific blue square KML style for easy identification on the map.

## 📊 Required CSV Structure
The Python scripts use `csv.DictReader`, which means your CSV headers **must match exactly** (case-sensitive and including spaces/symbols) with the scripts' expectations. 

Here are the required headers for each file:

### 1. `BAHAN_POLE.csv`
`Pole ID (New)`, `Coordinate (Lat) NEW`, `Coordinate (Long) NEW`, `Pole Provider (New)`, `Pole Type`, `LINE`

### 2. `BAHAN_FAT.csv`
`Pole ID (New)`, `Coordinate (Lat) NEW`, `Coordinate (Long) NEW`, `Pole Provider (New)`, `Pole Type`, `FAT ID/NETWORK ID`

### 3. `BAHAN_CH.csv`
`Clamp_Hook_ID`, `Clamp_Hook_LATITUDE`, `Clamp_Hook_LONGITUDE`

### 4. `BAHAN_HP.csv`
`HOMEPASS_ID`, `CLUSTER_NAME`, `PREFIX_ADDRESS`, `STREET_NAME`, `HOUSE_NUMBER`, `BLOCK`, `FLOOR`, `RT`, `RW`, `DISTRICT`, `SUB_DISTRICT`, `FDT_CODE`, `FAT_CODE`, `BUILDING_LATITUDE`, `BUILDING_LONGITUDE`, `Category BizPass`, `POST CODE`, `ADDRESS POLE / FAT`, `OV_UG`, `HOUSE_COMMENT_`, `BUILDING_NAME`, `TOWER`, `APTN`, `FIBER_NODE__HFC_`, `ID_Area`, `Clamp_Hook_ID`, `DEPLOYMENT_TYPE`, `NEED_SURVEY`

## 🚀 Prerequisites & Usage

To use this tool locally, you must have **Python** installed and configured on your environment. 

**Important Note before running:**
In `run_script.py`, the working directory is hardcoded:
`os.chdir(r"C:\Users\ihsan\Desktop\0. PROJECT\CSV TO KML")`
You **must change this path** to match the directory where you store your CSV and Python files on your machine.

1. Ensure your CSV files are placed in the correct working directory.
2. Run the main interface script:
   ```bash
   python run_script.py
   ```
3. A CLI menu will appear. Simply input the number corresponding to the script you want to run.

## 🌐 Web Application Alternative

I am currently working on a dedicated Web App version to handle this exact project workflow, removing the need to install Python locally.

It is not fully deployed yet, but you can check its future home here:
👉 [smallalley-linknet.verce.app](https://www.google.com/search?q=https://smallalley-linknet.verce.app)