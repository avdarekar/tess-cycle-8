import requests
from bs4 import BeautifulSoup as soup
from bs4.element import Tag
from io import TextIOWrapper
import numpy as np


def load_star_list(filepath: str) -> list[str]:
    """
    Read in text file containing list of stars.

    Arguments:
        filepath: file of path to list of star IDs

    Returns:
        stars: list of star IDs

    """

    try:
        with open(filepath, "r") as starlist:
            stars = starlist.readlines()
    except FileNotFoundError:
        print("File not found.")
        stars = []
    return stars


def open_file() -> TextIOWrapper:
    """
    Open file to write number of sectors to.

    Returns:
        file: new file to write to
    """

    filename = "TESS_number_of_sectors_cycle_8.txt"
    file = open(filename, "w")
    return file


def write_to_file(file: TextIOWrapper, text: str):
    """
    Write text to file.

    Arguments:
        file: file to write to
        text: text to write to file
    """
    file.write(text)


def get_table_rows(star: str) -> list[Tag]:
    """
    Submits POST request to URL, extracts table containing information
    about star ID including sectors, and gets rows from table.

    Arguments:
        star: string containing star ID

    Returns:
        table_rows: rows from table containing information about star ID
    """

    url = "https://heasarc.gsfc.nasa.gov/wsgi-scripts/TESS/TESS-point_Web_Tool/TESS-point_Web_Tool/wtv_v2.0.py/TICID_result"  # url for Web TESS Viewing Tool

    try:
        response = requests.post(url, data={"tic": star})
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

    else:
        page_soup = soup(response.text, "html.parser")
        table = page_soup.find(
            "table", class_="table table-striped table-hover"
        )

        if table:
            table_rows = table.find_all("tr")[1:]
        else:
            print("Table does not exist.")
            table_rows = []

    return table_rows


def get_sectors(table_rows: list[Tag]) -> list[int]:
    """
    Extract sectors from table.

    Arguments:
        table_rows: rows in table

    Returns:
        sectors: list of sectors extracted from table
    """
    sectors = []

    for row in table_rows:
        table_values = row.find_all("th")
        sectors.append(int(table_values[5].text.strip()))

    return sectors


def get_number_of_cycle_8_sectors(sectors: list[int]) -> int:
    """
    Return the number of sectors that are in cycle 8.

    Arguments:
        sectors: list of sectors

    Returns:
        number_of_sectors: number of sectors observed in cycle 8
    """

    sectors = np.array(sectors)
    number_of_sectors = len(
        np.where((sectors >= 97) & (sectors <= 107))[0]
    )

    return number_of_sectors


def get_number_of_sectors(filepath: str):
    """
    Get number of sectors a list of stars will be observed in cycle 8 of
    the TESS mission.

    Arguments:
        filepath: file path to list of star TIC IDs
    """

    stars = load_star_list(filepath)

    file = open_file()

    for star in stars:
        star = star.strip()
        write_to_file(file, star + " ")

        table_rows = get_table_rows(star)
        sectors = get_sectors(table_rows)
        number_of_sectors = get_number_of_cycle_8_sectors(sectors)
        write_to_file(file, str(number_of_sectors) + "\n")
        print(f"Wrote number of sectors in cycle 8 for TIC ID {star}")

    file.close()
    print("Finished writing file containing number of sectors in cycle 8")


# how to use script:
# get_number_of_sectors(r"data/TIC.txt")
