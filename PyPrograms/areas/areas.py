

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
    # select method
    print("\nwe can find area with following methods")
    print("1A - height and base (h, b)")
    print("1B - all 3 sides (a, b, c)")
    tritmp = input("how would you like to proceed?  ")
    print("") # get a new line
    if tritmp.upper() == '1A':
        h = int(input("h?  "))
        b = int(input("b?  "))
        area = 0.5*h*b
        print(f"area of triangle with (h,b) == ({h}, {b}) is {area}")
    elif tritmp.upper() == '1B':
        a = int(input("a?  "))
        b = int(input("b?  "))
        c = int(input("c?  "))
        s = (a + b + c) / 2
        area = (s*(s - a)*(s - b)*(s - c))**0.5
        print(f"area of triangle with sides ({a}, {b}, {c}) is {area}")

elif sipt == "2" :
    # get value of sides
    print() # get a new line
    side = float(input("What is size of side?  "))
    area = side**2
    print("Area of square is", area)

else :
    print("You have selected wrong option. Please select from a integer that has a shape associated with it")
