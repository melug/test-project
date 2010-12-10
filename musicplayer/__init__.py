import sys

def main():
    if len(sys.argv) == 1:
        showHelp()
    elif len(sys.argv) == 2:
        opt = sys.argv[1]
        if opt == '-l':
            showList()
        elif opt.startswith('http:'):
            playUri(opt)
        else:
            showHelp()
    elif len(sys.argv) == 3:
        opt = sys.argv[1]
        if opt == '-p':
            uriNumber = int(sys.argv[2])
            playNumber(uriNumber)
        else:
            showHelp()
    else:
        showHelp()

def showHelp():
    print '''
    shmusic [ stream_uri | -h | -l | -p number ]
    '''

def playUri(uri):
    print 'playing uri', uri

def playNumber(number):
    print 'playing #', number

def showList():
    print 'showing list'
