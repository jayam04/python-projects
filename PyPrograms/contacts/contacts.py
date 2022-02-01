# code by @JymPatel
# edited by @bupboi1337, (editors can put their name here && thanks for contribution :)

# this code uses GPL V3 LICENSE
print("this code uses GPL V3 LICENSE")
print("")

# start of code
# import library
import pickle

# get array from pickle data
infile = open('data/pickle-main', 'rb')
# defining array
# array[0] for first name, array[1] for last name, and so on..
array = pickle.load(infile)
infile.close()

print("update-22.02 ADDS SAVING YOUR DATA WHEN CLOSED BY OPTION 0\n##")


# making loop to run
loopvar = 0
while loopvar < 1:

    # ask user what to do
    print("")  # putting blank line before running new loop
    print("0.  exit program")
    print("1.  get all contacts")
    print("2.  add new contact")
    print("3.  sort contacts by first name")

    a = input("WHAT WOULD YOU LIKE TO DO?  ")

    # check for integer
    try:
        a = int(a)
    except ValueError:
        print("!! PLEASE ENTER AN INTEGRAL VALUE")

    # if option 1 is selected
    if a == 1:
        print("")
        print("== YOUR CONTACT LIST ==")
        print("")
        i1 = 0
        arraylen = len(array[0])
        # print all names
        while i1 < arraylen:
            print(f"{array[0][i1]} {array[1][i1]},  {array[2][i1]}  {array[3][i1]}")
            i1 += 1
        print("=======================")

    # option 2 is selected
    elif a == 2:
        # get a new contact
        array[0].append(input("First Name: "))
        array[1].append(input("Last Name: "))
        array[2].append(input("Phone Number: "))
        array[3].append(input("email ID: "))


    # if option 3 is selected
    elif a == 3:
        print("TODO")
        # TODO: fix sorting algo

    # if option 0 is selected
    elif a == 0:
        print("Saving your Data ...")
        outfile = open('data/pickle-main', 'wb')
        pickle.load(array, outfile)
        outfile.close()
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
