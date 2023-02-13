# PokerNow_Auto-Venmo
 For Fun Project allowing users to automatically pay and request after PokerNow games

To use this app, make an IDs.py file with your access_token, my_user_id, and ID_dict 
For your access_token:
'''
from venmo_api import Client
access_token = Client.get_access_token(username='USERNAME_HERE', password='PASSWORD_HERE')
'''
this will spit out information in your console. After 2FA, record the access-token in a string variable.

For my_user_id
'''
my_stuff = client.user.get_my_profile() #To get my stuff
print(my_stuff)
'''
Should pring out your user ID. Record this under the string variable my_user_id.
Finally, create a ID_dict with the format of {'FULL_NAME_IN_CAPITALS':'VENMO_USERNAME'}. Create as many entries as you want for your friends.

Once you are ready, Download the ledger from Poker_now and put it into a folder called CSV_Files.

At the top of Main.py, change Filename to the Filename of the file you just put in CSV_Files.
VenmoBalanceID, BofA_Checking_ID, and Santadner_ID are all optional variables. Just comment them out if you don't need it.
After all this is ready, hit run.

As the program cycles through the usernames, type in your Friend's actual name and Y to send/request money. Do this for all the friends until the program is finished running and your venmo should have automatically requested and sent money.
