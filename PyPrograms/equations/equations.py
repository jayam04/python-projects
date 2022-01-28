# code by @JymPatel
# edited by @bupboi1337, (editors can put their name here && thanks for contribution :)

# this code uses GPL V3 LICENSE
print("this code uses GPL V3 LICENSE")
print("")

# start of code

# what we can do
print("we can solve the following equations")
print("1  quadratic equation\n")
# take input
usrinput = input("what would you like to do?  ")

# for quadratic equation
if (usrinput == "1"):
	errorval = 0
	while errorval == 0:
		print("we would solve for quadratic equation 'ax^2 + bx + c'")
		# get values of a, b & c
		a = input("what is value of a?  ")
		b = input("what is value of b?  ")
		c = input("what is value of c?  ")
		# check for integers
		try:
			a = float(a)
			b = float(b)
			c = float(c)
			errorval += 1
		except ValueError:
			print("ERROR: INPUT MUST ONLY CONTAIN INTEGER OR FLOAT\n")
	# get value of D
	D = b**2 - 4*a*c
	if D >= 0:
		x1 = (-b + D)/(2*a)
		x2 = (-b - D)/(2*a)
		print(f"roots of equation are {x1}, {x2}")
	else:
		print(f"roots of your equations aren't real")
		print(f"rootS are {-b/(2*a)} +(i){D/(2*a)}, {-b/(2*a)} -(i){D/(2*a)}") # TODO FIX IT
	
# for linear equations with two variables

# if wrong option is selected
else:
	print("please enter a valid integer from tasks.")

# end of code
print("")
print("get this code at https://github.com/JymPatel/Python-FirstEdition")
