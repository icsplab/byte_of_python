print 'Simple Assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist

print 'Copy by making a full slice'
# make a copy by doing a full slice
mylist = shoplist[:]
del mylist[0]

print 'Shoplist is', shoplist
print 'mylist is', mylist