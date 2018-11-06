poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    # The 'line' already has a newline
    # at the end of each link
    # since it is reading from file.
    print line
f.close()