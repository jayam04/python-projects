import pickle


def getKEYchar(a, KEY):
    try:
        a = int(a)
        tmpVAR = int(KEY[a - 1]) * 1923
    except ValueError:
        tmpVAR = ord(KEY[a - 1]) * 125
    return tmpVAR



def getReminderPLUS(i, c):
    try:
        C = int(c) + 2
    except ValueError:
        C = ord(c) - 3
    if (C % i) == 0:
        return True
    else:
        return False



def encryptARRAY(array, KEY):
    # GET SOME VALUABLE VARIABLES
    KEYlen = len(KEY)
    encryptedARRAY = [[] for tmp in range(4)]
    totalContacts = len(array[0])
    for i in range(4):
        for j in range(totalContacts):
            encryptedARRAY[i].append([])
            # get string length
            Slen = len(array[i][j])
            for k in range(Slen):
                # get a space for encryption
                encryptedARRAY[i][j].append([])
                # ENCRYPTION RULES
                if (i + j*2 - k) % 3 == 0:
                    try:
                        tmpVAR3 = int(float(array[i][j][k])) * getKEYchar((i + j - k) % KEYlen, KEY) - 245 * (i + j + 7)
                        encryptedARRAY[i][j][k] = chr(tmpVAR3)
                    except ValueError or TypeError:
                        tmpVAR3 = ord(array[i][j][k]) + 11 + getKEYchar((i + k) % KEYlen, KEY) + (i + 5 - k)
                        encryptedARRAY[i][j][k] = tmpVAR3
                else:
                    encryptedARRAY[i][j][k] = array[i][j][k]
    return encryptedARRAY



def decryptARRAY(array, KEY):
    # GET SOME VALUABLE VARIABLES
    KEYlen = len(KEY)
    decryptedARRAY = [[] for tmp in range(4)]
    totalContacts = len(array[0])
    # LOOP FOR ALL TYPES
    for i in range(4):
        for j in range(totalContacts):
            decryptedARRAY[i].append([])
            # get string length
            Slen = len(array[i][j])
            for k in range(Slen):
                # get a space for encryption
                decryptedARRAY[i][j].append(array[i][j][k])
                # ENCRYPTION RULES
                if (i + j*2 - k) % 3 == 0:
                    try:
                        tmpVAR3 = int(array[i][j][k])
                        decryptedARRAY[i][j][k] = chr(tmpVAR3 - (i + 5 - k) - 11 - getKEYchar((i + k) % KEYlen, KEY))
                    except ValueError:
                        tmpVAR3 = ord(array[i][j][k])
                        decryptedARRAY[i][j][k] = int(tmpVAR3 + 245 * (i + j + 7)) / getKEYchar((i + j - k) % KEYlen,KEY)
    # CONVET DECRYPTED ARRAY TO STRINGS WHERE IT NEEDS AND RETURN NEW ARRAY
    finalARRAY = [[] for i in range(4)]
    for i in range(4):
        for j in range(totalContacts):
            finalARRAY[i].append([])
            finalARRAY[i][j] = ''
            Slen = len(decryptedARRAY[i][j])
            for k in range(Slen):
                finalARRAY[i][j] += str(decryptedARRAY[i][j][k])
    return finalARRAY



def getArray(KEY):
    # get array from pickle data
    infile = open('data/pickle-main', 'rb')
    # defining array
    array = pickle.load(infile)
    infile.close()
    # CHECK IF THERE IS ANY ENCRYPTION
    if KEY == 'noENCRYPTION':
        return array
    # IF IT IS GO ON YOUR WORK
    else:
        return decryptARRAY(array, KEY)



def saveData(array, KEY):
    # CHECK ENCRYPTION STATUS
    if KEY == 'noENCRYPTION':
        encryptedARRAY = array
    else:
        encryptedARRAY = encryptARRAY(array, KEY)
    # SAVE ENCRYPTED ARRAY USING PICKLE
    outfile = open('data/pickle-main', 'wb')
    pickle.dump(encryptedARRAY, outfile)
    outfile.close()