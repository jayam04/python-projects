def get_input(s):
    s = 'input.' + s
    infile = open(s, 'r')
    a = infile.read()
    infile.close()
    return a

def main():
    S = get_input('txt')
    Slen = len(S)
    outcode = ''
    for i in range(Slen):
        VAR = ord(S[i])
        outcode += '>'
        for j in range(VAR):
            outcode += '+'
        outcode += '.'
    print(outcode)
    outfile = open('output.bf', 'w')
    outfile.write(outcode)
    outfile.close()
    return


main()