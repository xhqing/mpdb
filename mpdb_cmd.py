import os, sys
from bdb import BdbQuit

def main():
    try:
        os.mkfifo('p_in')
    except:
        pass

    try:
        os.mkfifo('p_out')
    except:
        pass

    os.system("cat p_out &")
    f_pin = open('p_in','w')
    while True:
        string = sys.stdin.readline()
        f_pin.write(string)
        f_pin.flush()
        if string[0] == 'q': 
            os.unlink('p_in')
            os.unlink('p_out')
            raise BdbQuit

if __name__=='__main__':
    main()

