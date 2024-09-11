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


# Getting the download urls for files uploaded by user on wix site
def get_data():
    json_vars = os.getenv('JSON_VARS')
    urls_dict = json.loads(json_vars)  # Decode JSON string into a dictionary
    download_url1 = urls_dict['downloadUrl1']
    download_url2 = urls_dict['downloadUrl2']
    return download_url1, download_url2


def get_file(url):
    pass
