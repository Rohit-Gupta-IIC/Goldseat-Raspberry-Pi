import sys

# count the arguments
arguments = len(sys.argv) - 1

# output argument-wise
position = 1
while (arguments >= position):
    print ("parameter %i: %s" % (position, sys.argv[position]))
    position = position + 1
