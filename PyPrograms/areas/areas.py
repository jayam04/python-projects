

# it uses GPL V3 LICENSE
# what we are going to do
print("We can find areas of different shapes from below")

# shapes we have
print("1. Triangle")
print("2. Square")

# take input
sipt = input("For what you would like to find area?")

# if 1 is sel
if sipt == "1" :
    print("coming soon")

elif sipt == "2" :
    # get value of sides
    side = float(input("What is size of side?"))
    area = side**2
    print("Area of square is", area)

else :
    print("You have selected wrong option. Please select from integer that has some shape associated with it")
