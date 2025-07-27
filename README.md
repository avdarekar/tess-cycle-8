# tess_c3

## Description 
This program uses the [Web TESS Viewing Tool](https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/) to count how many sectors a star will be observed in cycle 8. 

## Table of Contents
- File Descriptions
- Obtaining Data
- Installation 
- Usage

## File Descriptions
- TIC.txt: This file is a sample text file containing star TIC IDs that you can use to run tess_cycle_8.py on.
- tess_cycle_8.py: This script uses the Web TESS Viewing Tool to find the number of sectors each star will be observed in cycle 8. It writes all of this information to TESS_number_of_sectors_cycle_8.txt. 
- TESS_number_of_sectors_cycle_8.txt: This is the text file that the tess_cycle_8.py program writes to.

## Obtaining Data
The data is obtained using the [Web TESS Viewing Tool](https://heasarc.gsfc.nasa.gov/cgi-bin/tess/webtess/wtv.py). 

## Installation 
To successfully run this program locally, clone this repo and install requirements in a virtual environment using the requirements.txt file.

## Usage
After installation, run the get_number_of_sectors() function in tess_cycle_8.py. 
