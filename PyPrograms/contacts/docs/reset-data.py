array = [['Jym'], ['Patel'], [''], ['jympatel@yahoo.com']]

import pickle
outfile = open('data/pickle-main', 'wb')
pickle.dump(array, outfile)
outfile.close()