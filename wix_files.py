import requests
import pandas as pd
from io import BytesIO
from io import StringIO
import chardet


"""
This file includes functions to download and create dataframe from a file uploaded by user  
on wix site. It includes identifying file extensions (csv, Excel), encoding detection for
csv files and conversion to utf-8 if needed
"""


# downloading file that user uploaded on wix, checking which type (Excel or csv) and making Dataframe
def download_wix_file(download_url):
    # Map of common Content-Types to file extensions
    content_type_map = {
        'application/pdf': '.pdf',
        'image/jpeg': '.jpg',
        'image/png': '.png',
        'application/zip': '.zip',
        'text/html': '.html',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': '.xlsx',  # For .xlsx (Excel)
        'application/vnd.ms-excel': '.xls',  # For older .xls (Excel)
        'text/csv': '.csv',  # For CSV files
        'application/msword': '.doc',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document': '.docx',  # Word document (.docx)
        'application/json': '.json',  # JSON
        # Add more Content-Type mappings as needed
    }

    try:
        # Send a GET request to the download URL
        response = requests.get(download_url, stream=True)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the Content-Type (file type) from the headers
            content_type = response.headers.get('Content-Type')
            # Map the Content-Type to a file extension
            file_extension = content_type_map.get(content_type, '')
            if file_extension == '.xlsx':
                # Reads Excel file and returns dataframe
                df = read_excel(response)
                return df
            if file_extension == '.csv':
                # Reads csv file and returns dataframe
                df = read_csv(response)
                return df

            if not file_extension or file_extension not in ['.xlsx', '.csv']:
                # Point to code that returns POST to wix saying file 'no good'
                return 'no good'

        else:
            print(f"Failed to download file. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Reading Excel file from file uploaded by user on wix
def read_excel(response):
    # Use BytesIO to load the content into memory as a file-like object
    excel_data = BytesIO(response.content)
    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_data)
    return df


# Checking csv file encoding and if necessary changing to utf-8
def encoding_csv(response):
    # Detect the encoding of the file using chardet
    raw_data = response.content
    detected_encoding = chardet.detect(raw_data)['encoding']
    print(f"Detected encoding: {detected_encoding}")
    # Decode content to string using detected encoding (if not None) and re-encode as utf-8
    if detected_encoding:
        text_data = raw_data.decode(detected_encoding)
    else:
        print("Could not detect encoding, using utf-8 by default.")
        text_data = raw_data.decode('utf-8')
    return text_data


# Reading csv file from file uploaded by user on wix
def read_csv(response):
    # checking csv file encoding
    text_data = encoding_csv(response)
    # Use StringIO to load the content into memory as a file-like object
    csv_data = StringIO(text_data)
    # Load the CSV content into a pandas DataFrame
    df = pd.read_csv(csv_data)
    return df
