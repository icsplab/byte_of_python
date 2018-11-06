import pickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = open(shoplistfile, 'wb')

# Dump the object to a file, and write?
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
# Load the object from file
storedlist = pickle.load(f)
print storedlist