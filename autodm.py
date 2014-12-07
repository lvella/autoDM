from treasure import *
import armor

def format(res, ident = ''):
    if res:
        if isinstance(res, list):        
            for e in res:
                format(e, ident)

        elif isinstance(res, tuple):
            name, val = res
            if name:
                print ident + name + ':'
                ident = ident + '  '
            format(val, ident)

        else:
            print ident + res

for i in xrange(2):
    format(armor.minor.run())
    #format(treasure.run())
