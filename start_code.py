#!/usr/bin/python
# -*- encoding: utf-8 -*-

def checkio(data):

    #replace this for solution
    return []


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert(checkio( '002080629173140807EDF27C1E3E9701') ==
        ['26 Aug 2002 19:37:41 GMT +20', 7, 'message']), "First Test"

    assert(checkio('003170502011718208D7327BFC6E9743') ==
        ['05 Jul 2013 02:11:17 GMT +7', 8, 'Welcome!']), "Second Test, 7 bit"

    assert(checkio('000130925161956915C8729E054A82C26D50DA0D7296EFA0EC5BBE06') ==
        ['2010-03-29 15:16:59 GMT -4', 21, 'Hey, I am in New York']), "Third Test, negative timezone"
