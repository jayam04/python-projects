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
array = pickle.load(infile)
infile.close()

print("update-22.02 ADDS SAVING YOUR DATA WHEN CLOSED BY SAVING USING OPTION 0\n##")

# for ease in reading
fname = 0
lname = 1
number = 2
email = 3
# getting some variables
promptvar = 0 # variable for prompt
loopvar = 0 # variable for main loop
# making loop to run
while loopvar < 1:
    # ask user what to do
    print("")  # putting blank line before running new loop
    if promptvar == 0:
        print("0.  exit program")
        print("1.  get all contacts")
        print("2.  add new contact")
        print("3.  sort contacts by first name")
        print("9.  stop getting this prompt")

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
        arraylen = len(array[fname])
        # print all names
        while i1 < arraylen:
            print(f"{array[fname][i1]} {array[lname][i1]},  {array[number][i1]}  {array[email][i1]}")
            i1 += 1
        print("=======================")

    # option 2 is selected
    elif a == 2:
        # get a new contact
        array[fname].append(input("First Name: "))
        array[lname].append(input("Last Name: "))
        array[number].append(input("Phone Number: "))
        array[email].append(input("email ID: "))

    # if option 3 is selected
    elif a == 3:
        print("TODO")
        # TODO: fix sorting algo

    # option 9
    elif a == 9:
        # change prompt settings
        if promptvar == 0: 
            promptvar += 1
            print("you won't get prompt now!")
            print("ENTER 9 AGAIN TO START GETTING PROMPT AGAIN!!")
        else:
            promptvar -= 1


    # if option 0 is selected
    elif a == 0:
        print("Saving your Data ...")
        outfile = open('data/pickle-main', 'wb')
        pickle.dump(array, outfile)
        outfile.close()
        print("YOUR DATA HAS BEEN SAVED SUCESSFULLY!")
        loopvar += 1

    # if no true option is selected
    else:
        print("!! PLEASE ENTER VALUE FROM GIVEN INTEGER")

# end of code
print("")
print("get this code at https://github.com/JymPatel/Python-FirstEdition")
