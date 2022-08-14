#!./.venv/bin/python3

# # this code is licensed under GNU General Public License v3 (#TODO)

import sys
import pickle
from datetime import datetime
from termcolor import colored


# defining global variables (will be overwrite by main() at initial run)
users = [] # stores identities of users
transactions = [] # stores all transactions done
# other variables
data_folder = "data/"



class Transaction:
    # object that stores details of one transaction
    def __init__(self, amount, user_id, description=None):
        # add time and description
        self.time = datetime.now()
        self.description = description
        # add transaction number
        ... # TODO add self.transact attribute
        # add transfer amount
        try:
            self.amount_change = float(amount)
        except ValueError:
            raise ValueError("amount is not float!")
        # add user.ID if valid user exists
        for user in users:
            if user.ID == user_id:
                user.ID = self.transact_number
                self.user = user.ID
        else:
            raise IndexError("Invalid User ID!")


class Person:
    # a person has name, id, transactions
    def __init__(self, first, last, middle, entered_ID, balance=0):
        self.balance = balance
        self.transactions = [] # stores transactions of class Transaction
        # set Person name
        if middle:
            self.name = f"{first} {middle} {{last}}"
        else:
            self.name = f"{first} {last}"
        # set Person id
        try:
            self.ID = entered_ID
        except ValueError:
            raise ValueError("user ID already taken!")

    # check if ID is unique
    @property
    def ID(self):
        return self._id
    
    @ID.setter
    def ID(self, id):
        if id not in [user._id for user in users]:
            self._id = id
        else:
            raise ValueError("user ID already taken!")

    # print user data when told to
    def print_data(self):
        print(f"{self.name} with userID {self.ID} has balance of {self.balance}")



def main():
    task = get_task()
    
    if task == "version":
        print(f"manager.py\ncurrent version {current_version()}")
    elif task == "help":
        get_help()
    elif task == "newaccount":
        users.append(create_user())
        print(colored(f"created account for {users[-1].name} with UNIQUE ID {users[-1].ID} and balance {users[-1].balance}", "green"))
    elif task == "transact":
        new_transaction = create_transaction()

    elif task == "listusers":
        print('users with us ...')
        for user in users:
            user.print_data()


def get_task(): # returns task, takes input from command line (arg while running program)
    try: 
        task =  sys.argv[1]

        if task in ["-h", "--help", "help"]:
            return "help"
        elif task in ["-v", "--version", "version"]:
            return "version"
        elif task in ["newaccount", "transact", "listusers"]:
            return task


        else: # else return error 102 in RED
            generated_error = "ERROR 102\nCould not find task provided\nTry manager.py --help"
            sys.exit(colored(generated_error, "red"))

    except IndexError: # no arguements given
        generated_error = "ERROR 101\nInsufficient argurments\nTry manager.py --help"
        sys.exit(colored(generated_error, "red"))



def create_user(): # returns user of type Person created by taking input from user
    first = input("First Name: ")
    middle = input("Middle Name: ")
    last = input("Last Name: ")
    while True:
        try:
            unique_id = input("create userID: ")

            if unique_id == "": # empty ID
                print(colored("you can't use empty string!", "red"))
                continue

            user = Person(first, last, middle, unique_id)
            break

        except ValueError:
            print(colored("userID already taken, try another!", "red"))
            continue
    return user


def create_transaction(): # creates a new transaction
    ... # TODO create transaction function



def load_data(): # loads data while starting program
    global users 
    global transactions
    try:
        users = pickle.load(open(data_folder + "users.pickle", "rb"))
    except FileNotFoundError:
        print(colored(f"user.picklenot found in {data_folder}", "red"))
        if input("would you like to RESET data? y/n: ").lower() in ["yes", "y", "yeah"]:
            reset_datafile(data_folder + "users.pickle")
    try:
        transactions = pickle.load(open(data_folder + "transactions.pickle", "rb"))
    except FileNotFoundError:
        print(colored(f"transactions.pickle not found in {data_folder}", "red"))
        if input("would you like to RESET data? y/n: ").lower() in ["yes", "y", "yeah"]:
            reset_datafile(data_folder + "transactions.pickle")

def reset_datafile(location): # reset storage file to default (empty)
    file = open(location, "wb")
    pickle.dump([], file)
    file.close()

def save_data(): # saves new transactions, users, more while exiting program
    with open(f"{data_folder}users.pickle", "wb") as users_file:
        pickle.dump(users, users_file)
    with open(f"{data_folder}transactions.pickle", "wb") as transactions_file:
        pickle.dump(transactions, transactions_file)



def get_help(): # opens help doc and prints it
    print(colored("\nopening docs/help ...", "yellow"))
    print(open("./docs/help.txt", 'r').read())

def current_version(): # returns string of current version
    major = 1
    minor = 1
    return f"{major}.{minor}"


if __name__ == '__main__':
    load_data()
    main()
    save_data()
    # end
    print(colored("\nthis code is licensed under GNU General Public License v3", "blue"))
    print(colored("get this code at https://github.com/JymPatel/useless-manager", "blue"))