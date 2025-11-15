# tess-cycle-8

## Description 
This program uses the [Web TESS Viewing Tool](https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/) to count how many sectors a star will be observed in cycle 8. 

## File Descriptions
- tess_cycle_8.py: this script uses the Web TESS Viewing Tool to find the number of sectors each star will be observed in cycle 8
- requirements.txt: contains required Python packages 

### data 
- TIC.txt: this file is a sample text file containing star TIC IDs that you can use to run tess_cycle_8.py on
- TESS_number_of_sectors_cycle_8.txt: this is the text file that the tess_cycle_8.py program writes to

## Obtaining Data
The data is obtained using the [Web TESS Viewing Tool](https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/). 

## Installation 
To successfully run this program locally, clone this repo and install requirements in a virtual environment using the requirements.txt file.

## Usage
After installation, run the get_number_of_sectors() function in tess_cycle_8.py. 
