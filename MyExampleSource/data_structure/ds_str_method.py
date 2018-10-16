name = 'ijpark'

if name.startswith('I am'):
    print 'Yes, the string start with "I am"'

if 'a' in name:
    print 'Yes, it contain the string "a"'

if name.find("jpa") != -1:
    print 'Yes, it contains the string "jpa"'

delimiter ='_*_'
mylist = ['Brazil', 'Russia', 'India', 'Korea']
print delimiter.join(mylist)
