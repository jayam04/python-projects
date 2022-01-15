# project by Jym Patel
# it uses GPL v3 License

# defining array
fname = ["Jym"]
lname = ["Patel"]
number = [""]
email = ["jympatel@yahoo.com"]
    
print("CLOSING PROGRAM WILL RESET ALL CHANGES MADE IN YOUR CONTACT LIST\n##")


# making loop to run
loopvar = 0
while loopvar < 1:
    
    # ask user what to do
    print("") # putting blank line before running new loop
    print("What you would like to do?")
    print("0.  exit program")
    print("1.  add new contact")
    print("2.  get all contacts")
    
    a = input("")
    
    # check for integer
    try:
        a = int(a)
    except ValueError:
        print("please enter an integral value")
    
    # option 1 is selected
    if a == 1:
        # get a new contact
        fname.append(input("First Name: "))
        lname.append(input("Last Name: "))
        number.append(input("Phone Number: "))
        email.append(input("email: "))
        
    # if option 2 is selected
    elif a == 2:
        print("")
        print("== YOUR CONTACT LIST ==")
        print("")
        i1 = 0
        i2 = len(fname)
        # print all names
        while i1 < i2:
            print(fname[i1], lname[i1], number[i1], email[i1])
            i1 += 1
        print("")
        print("=======================")
        
    # if option 0 is selected
    elif a == 0:
        print("DO YOU REALLY WANT TO EXIT")
        print("YOUR DATA SAVED IN CONTACTS WILL BE RESETED")
        
        # conform & exit
        inpt = input("y/n? ")
        if inpt == 'y' or inpt == 'Y':
            loopvar += 1
            print("get it at https://github.com/JymPatel/Python-FirstEdition")
        
    else:
        print("enter value from any one option")
