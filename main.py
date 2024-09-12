"""
This program matches two sets according to the preferences of the elements in each set -
a list of open positions with preferences for specific candidates and a list of candidates
with preferences for specific open positions.
The frontend is a wix site that interacts with the user, gets files from user and invokes GitHub
workflow action to run this python code.
At the end of the match process (the python code) a file with the results is saved in GitHub repo
for download by the user through the wix site. The results are also send from the python code to
the wix site using wix site API (http requests) and presented on the site to user
"""

import pandas as pd
import os
import json
import requests

from wix_files import download_wix_file
from data_tests import data_integrity


# Getting the download urls for files uploaded by user on wix site
# and transferred through request on wix server side to activate GitHub workflow action
def get_data():
    try:
        json_vars = os.getenv('JSON_VARS')
        urls_dict = json.loads(json_vars)  # Decode JSON string into a dictionary
        download_url1 = urls_dict['downloadUrl1']
        download_url2 = urls_dict['downloadUrl2']
        return download_url1, download_url2
    except Exception as e:
        print(f"An error occurred: {e}")


# The main function running the integrated process
def run_match_app():
    # Getting wix download urls
    download_url1, download_url2 = get_data()

    # Making dataframes from the wix files
    df1 = download_wix_file(download_url1)
    df2 = download_wix_file(download_url1)

    # Testing data in dataframes
    message, result = data_integrity(df1, df2)
    if result != 0:
        # Here goes code to return error to wix
        pass

    # Run match process


if __name__ == '__main__':
    run_match_app()