# by @JymPatel
# Note: This program is licenced under GPL V3.

# edited by ... (editors can put their name and thanks for suggestion) :)
# @bupboi1337


# what we are going to do
print("We can solve the below equations")
print("1  Quadratic Equation")
print("2  Linear Equations with two Variables")

# ask what they want to solve
sin = input("What you would like to solve?")

try:
    sin = int(sin)
except ValueError:
    print("Please enter a valid INTEGER")

# for Qdc Eqn
if sin == '1':
    print("We will solve for equation 'a(x^2) + b(x) + c'")

    # take some user input
    a = float(input("What is value of a?"))
    b = float(input("What is value of b?"))
    c = float(input("What is value of c?"))

    D = b**2 - 4*a*c

    if D < 0:
        print("No real values of x satisfies your equation.")

    else:
        x1 = (-b + D)/(2*a)
        x2 = (-b - D)/(2*a)

        print("Roots for your equation are" , x1, "&", x2) # output root numbers for equation
        

        
# for Lnr Eqn (2 var)        
if sin == '2' :
    print("We will solve for equations a1(x) + b1(y) + c1 & a2(x) + b2(y) + c2")
    
    # take some more user input
    a1 = float(input("Put value of a1"))
    b1 = float(input("Put value of b1"))
    c1 = float(input("Put value of c1"))
    a2 = float(input("Put value of a2"))
    b2 = float(input("Put value of b2"))
    c2 = float(input("Put value of c2"))
    
    # for infinite or no solution
    if (a1/a2) == (b1/b2) :
        if (a1/a2) == (c1/c2) :
            print("Infinite set of values satisfies your equation.")
        if (a1/a2) != (c1/c2) :
            print("No values of variables satisfies your equation.")
    
    else :
        x = (b2*c1 - b1*c2)/(a2*b1 - a1*b2)
        y = (a2*c1 - a1*c2)/(b2*a1 - b1*a2)
        
        print("(", x, ",", y, ")", 'is solution for your equation') # print soulution



else: # error message
    print("You have selected wrong option.")
    print("Select a integer for your equation and run this code again")



# end of code and link to this repo
print("You can visit https://github.com/JymPatel/Python3-FirstEdition")
