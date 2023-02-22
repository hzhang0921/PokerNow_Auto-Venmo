from Data_parser import *
from Venmo_API import *
import IDs
from venmo_api import Client
access_token = 'f271d00c4d963be602fe3a4cd2921a0da741d7ee9b730908c6669c7c8b8949a3'
client = Client(access_token=access_token)
Venmo_balance_id = IDs.Venmo_balance_id
BofA_Checking_id = IDs.BofA_Checking_id
Santander_id = IDs.Santander_id

Filename = "Feb8Ledger.csv"

def main():
    dict = Data(Filename) #sets what .csv file you want to pay from
    os.chdir("/Users/haoyang/Documents/VScode/Python/PokerNow_Auto-Venmo")
    for keys in dict:
        print(f"Enter the name for {keys}: ")
        name = str(input()).upper()
        if name == "HAOYANG ZHANG" or name == "SKIP":
            continue
        elif name not in IDs.ID_dict:
            response = input('name not found in dictionary. To continue, type "continue", else type "stop" to stop and fix the dictionary: ')
            if response == "continue":
                print(f"{name} will pay another way")
                continue
            elif response == "stop":
                break
            else:
                break
        else:
            user = get_user_by_username(IDs.ID_dict[name])
            id = user.id
            Name_from_id = user.first_name + " " + user.last_name
            if dict[keys] > 0:
                print(f"you are paying {Name_from_id} ${dict[keys]}. Are you sure? Y/N ")
                confirmation = input()
                if confirmation == "Y" or confirmation == "y":
                    #Send_specific(dict[keys], "Congrats!", get_user_by_username(IDs.ID_dict[name]).id, Venmo_balance_id)
                    print(f"payment completed for {Name_from_id} for ${dict[keys]}")
                else:
                    print(f"payment not complete.")
                    continue
            elif dict[keys] < 0:
                print(f"you are requesting ${dict[keys]*-1} from {Name_from_id}. Are you sure? Y/N ")
                confirmation = input()
                if confirmation == "Y" or confirmation == 'y':
                    #Request(dict[keys]*-1, "Unlucky Rubber Ducky", get_user_by_username(IDs.ID_dict[name]).id)
                    print(f"payment successfully requested from {Name_from_id} for ${dict[keys]*-1}.")
                else:
                    print(f"payment failed to request.")
                    continue
            else:
                continue

if __name__ == "__main__":
    main()

