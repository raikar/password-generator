#!/usr/bin/python

import os
import random
import sys

c = 'abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-+='

p = ''

if len(sys.argv) > 1:
    try:
        l = int(sys.argv[1])
    except ValueError:
        print 'Usage: %s [<length>]' % os.path.basename(sys.argv[0])
        sys.exit()
else:
    l = 12

for i in range(l):
    random.seed()
    p += random.choice(c)

print p
