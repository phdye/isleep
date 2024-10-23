#------------------------------------------------------------------------------

import sys

def test_syspath():

    print(': import paths')
    for path in sys.path :
        print(path)
    print(': - - - - -')
    print('')
    sys.stdout.flush()
    
    assert False

#------------------------------------------------------------------------------
