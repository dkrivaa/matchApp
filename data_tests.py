import pandas as pd


"""
This file checks the integrity of the data contained in the files uploaded by user on wix site.
The checks include:
1. The length of df1 (number of open positions) is smaller or equal to length of df2 (number
of candidates).
2. no double entries in preferences 
3. preferences are consistent with names in other dataframe set 
"""


def test1(df1, df2):
    return [0 if len(df1) <= len(df2) else 1][0]


def test2(df):
    # Iterate over each row
    for index, row in df.iterrows():
        # Slice the row from the 2nd column to the last
        row_slice = row[1:]  # Exclude the first column
        # Check if there are duplicates
        return [1 if row_slice.duplicated().any() else 0][0]


def test3(df_1, df_2):
    df_1_names = df_1.iloc[:, 0].tolist()  # Correcting the list conversion
    for index, row in df_2.iterrows():
        # Slice the row from the 2nd column to the last
        row_slice = row[1:]  # Exclude the first column
        # Check if all items in row_slice are in df_1_names
        if not all(item in df_1_names for item in row_slice):
            return 1  # Return 1 if any row contains an item not in df_1_names
    return 0  # Return 0 if all rows meet the condition


def data_integrity(df1, df2):
    check1 = test1(df1, df2)
    if check1 == 0:
        check2_df1 = test2(df1)
        if check2_df1 == 0:
            check2_df2 = test2(df2)
            if check2_df2 == 0:
                check3_df1 = test3(df1, df2)
                print('printing the result of df_1_names', check3_df1)
                if check3_df1 == 0:
                    check3_df2 = test3(df2, df1)
                    if check3_df2 == 0:
                        return 'all_tests', 0
                    else:
                        return 'Preferences in file 1 are not consistent with names in file 2', 1
                else:
                    return 'Preferences in file 2 are not consistent with names in file 1', 1
            else:
                return 'Identical entries in preferences in file 2', 1
        else:
            return 'Identical entries in preferences in file 1', 1
    else:
        return 'Number of entries in file 2 is smaller than entries in file 1', 1






