from venmo_api import Client
import pprint
import IDs

access_token = IDs.access_token
ID_dict = IDs.ID_dict
my_user_id = IDs.my_user_id
Venmo_balance_id = IDs.Venmo_balance_id

client = Client(access_token=access_token)

# All callable user. about, date_joined, display_name, first_name, from_json, 
# id, is_active, is_group, last_name, phone, profile_picture_url, to_json, username

def Search(Name): #Used for searching for User_IDs str
    users = client.user.search_for_users(query = Name) 
    for user in users: 
        print(user.first_name + " " + user.last_name + " :" + user.id)

def View_payment_methods():
    payment_methods = client.payment.get_payment_methods() # Views your current payment methods
    print(dir(payment_methods))
    for payment_method in payment_methods:
        pprint.pprint(payment_method.to_json())

def my_stuff(): #Function for viewing my imformation 
    my_stuff = client.user.get_my_profile() 
    print(my_stuff)

def get_my_friends():
    users = client.user.get_user_friends_list(user_id=my_user_id) #getting the friend's list of whatever user_id you set
    for user in users:
        print(user.username + " " + user.first_name + " " + user.last_name + ": " + str(user.id))
    

# Request money
def Request(amount, message, user_id): #amount is value, message is the request message, user_id is the user_id of the person you are requestion from int, str, str
    client.payment.request_money(amount, message, user_id)

# Send money (with default payment method)
def Send(amount, message, user_id): #int str str
    client.payment.send_money(amount, message, user_id)

# Send money (with the provided payment method id)
def Send_specific(amount, message, user_id, fund_id): #int str str str
    client.payment.send_money(amount=amount, note=message, target_user_id=user_id, funding_source_id=fund_id)


def callback(transactions_list): #Complementary function for get_transactions
    for transaction in transactions_list:
            print(transaction)

def get_transactions(target_user_id): #target_user_id is an str
    client.user.get_user_transactions(user_id=target_user_id, callback=callback)
    

def get_user_by_username(User_name): #str
    user = client.user.get_user_by_username(User_name)
    return user
#Use Dir to find the functions of a class

def check_ID_dict(Dict): #Used to verify all the dict entries in IDs
    for keys in Dict:
        print(get_user_by_username(Dict[keys]).first_name + " " + get_user_by_username(Dict[keys]).last_name)



def main():
    check_ID_dict(IDs.ID_dict)
    pass
    
if __name__ == "__main__":
    main()