import pandas as pd


def prepare_results(couples, file1_summary, file2_summary):

    # Create a list of dictionaries for 'couples'
    couples_list = [{"file1": lead, "file2": compliment} for lead, compliment in couples]
    file1_summary_dict = {'success': file1_summary[0],
                          'total': file1_summary[1]}
    file2_summary_dict = {'success': file2_summary[0],
                          'total': file2_summary[1]}
    results = {
        'couples': couples_list,
        'file1_summary': file1_summary_dict,
        'file2_summary': file2_summary_dict
    }

    return results
