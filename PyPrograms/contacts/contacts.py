# code by @JymPatel
# edited by (editors can put their name here && thanks for contribution :)

# this code uses GPL V3 LICENSE
print("this code uses GPL V3 LICENSE")
print("")

# start of code
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
    print("WHAT WOULD YOU LIKE TO DO?")
    print("0.  exit program")
    print("1.  add new contact")
    print("2.  get all contacts")
    print("3.  sort contacts by first name")

    a = input("")

    # check for integer
    try:
        a = int(a)
    except ValueError:
        print("!! PLEASE ENTER AN INTEGRAL VALUE")

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
        print("=======================")

    # if option 3 is selected
    elif a == 3:
        for i in range(len(fname) - 1):
            if (fname[i] > fname[i - 1]):
                # interchange names
                tmpfnme = fname[i]
                tmplnme = lname[i]
                tmpmail = email[i]
                tmpcont = number[i]
                fname[i] = fname[i - 1]
                lname[i] = lname[i - 1]
                number[i] = number[i - 1]
                email[i] = email[i - 1]
                fname[i - 1] = tmpfnme
                lname[i - 1] = tmplnme
                number[i - 1] = tmpcont
                email[i - 1] = tmpmail
        print("contacts are sorted now!")

    # if option 0 is selected
    elif a == 0:
        print("DO YOU REALLY WANT TO EXIT")
        print("YOUR DATA SAVED IN CONTACTS WILL BE RESETED")

        # conform & exit
        inpt = input("y/n? ")
        if inpt == 'y' or inpt == 'Y':
            loopvar += 1

    # if no true option is selected
    else:
        print("!! PLEASE ENTER VALUE FROM GIVEN INTEGER")

# end of code
print("")
print("get this code at https://github.com/JymPatel/Python-FirstEdition")
