import pandas as pd
import os
from csv import DictReader
import pprint

#The following function takes a file_name of .csv filetype from PokerNow and converts it into a simplified dictionary for usage
#The Keys are the Usernames used by individuals, the values are money gained or lost

def Data(file_name):
    os.chdir("/Users/haoyang/Documents/Coding/Python/PokerNow_Auto-Venmo")
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # df = pd.read_csv("Sample_Ledger.csv").to_string().split()
    
    csv_name = file_name
    with open(csv_name, 'r') as data:
        dict_reader = DictReader(data)
        list_of_dict = list(dict_reader)

    new_dict = {}
    for dicts in list_of_dict:
        if dicts['player_id'] not in new_dict:
            new_dict[dicts['player_id']] = [float(dicts['net'])/100, dicts['player_nickname']]
        else:
            new_dict[dicts['player_id']] = [new_dict[dicts['player_id']][0] + float(dicts['net'])/100, new_dict[dicts['player_id']][1]]
    
    pprint.pprint(new_dict)
    nickname_dict = {}
    for keys in new_dict:
        if new_dict[keys][1] not in nickname_dict:
            nickname_dict[new_dict[keys][1]] = new_dict[keys][0]
            
    # pprint.pprint(nickname_dict)        
    return(nickname_dict)
    




