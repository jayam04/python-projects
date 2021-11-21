# this uses GPL V3 LICENSE

binary = '$'
n = 15

try:
    input = int(input("What is your Decimal Number?"))
    limit = 65536
    input <= limit
except ValueError:
    print("Please put integer in input! & less than", limit)
    sys.exit()
    
while n >= 0:
    if input < 2**n:
        binary = binary + '0'
    else:
        binary = binary + '1'
        input = input - 2**n
    n = n - 1

print(binary)
