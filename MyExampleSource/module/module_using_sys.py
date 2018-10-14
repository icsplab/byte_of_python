import sys
import os


print('The command line arguments are:')
for i in sys.argv:
    print i

print '\n\nThe PYTHONE PATH is', sys.path, '\n'

print sys.argv[0]
print 'sys.path[0]', sys.path[0]
print 'sys.path[1]', sys.path[1]
print 'sys.path[2]', sys.path[2]

print os.getcwd()