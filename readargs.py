import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

def add():
	return sys.argv[1]+sys.argv[2]

print(add())