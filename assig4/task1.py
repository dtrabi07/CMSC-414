import binascii
import sys
import argparse



def task1(c1bin,c2bin,guessbin,offset):
    #note all three of c1bin, c2bin,guessbin have been converted into python3 bytes objects
    output = bytearray(c2bin)

    # YOUR CODE HERE. It should compute some output possibly as an XOR of something.
    gLen = len(guessbin)
    v1 = []
    for a, b in zip(c1bin, c2bin):
        v1.append(a ^ b)

    v2 = []  # XOR key with guess
    
    # for i in range(60):
    #myAscii = ""
        # v2 = []
    v3 = v1[offset:offset+gLen]
    for d, n in zip(v3, guessbin):
        v2.append(d ^ n)
    
    v4 = output[1:offset]
    v4 = v4 + bytearray(v2)
    v5 = v4 + output[offset+gLen:len(output)]
    
    output = v5

    print(output) # you probably want to print whatever you do. Note python will escape binary that doesn't correspond to valid printable ascii.\
                  # you may want to do something else in terms of printing
    return output # make sure you return the result for the auto grading 

#  $$$$$$$\   $$$$$$\        $$\   $$\  $$$$$$\ $$$$$$$$\       $$\      $$\  $$$$$$\  $$$$$$$\  $$$$$$\ $$$$$$$$\ $$\     $$\
#  $$  __$$\ $$  __$$\       $$$\  $$ |$$  __$$\\__$$  __|      $$$\    $$$ |$$  __$$\ $$  __$$\ \_$$  _|$$  _____|\$$\   $$  |
#  $$ |  $$ |$$ /  $$ |      $$$$\ $$ |$$ /  $$ |  $$ |         $$$$\  $$$$ |$$ /  $$ |$$ |  $$ |  $$ |  $$ |       \$$\ $$  /
#  $$ |  $$ |$$ |  $$ |      $$ $$\$$ |$$ |  $$ |  $$ |         $$\$$\$$ $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$$$$\      \$$$$  /
#  $$ |  $$ |$$ |  $$ |      $$ \$$$$ |$$ |  $$ |  $$ |         $$ \$$$  $$ |$$ |  $$ |$$ |  $$ |  $$ |  $$  __|      \$$  /
#  $$ |  $$ |$$ |  $$ |      $$ |\$$$ |$$ |  $$ |  $$ |         $$ |\$  /$$ |$$ |  $$ |$$ |  $$ |  $$ |  $$ |          $$ |
#  $$$$$$$  | $$$$$$  |      $$ | \$$ | $$$$$$  |  $$ |         $$ | \_/ $$ | $$$$$$  |$$$$$$$  |$$$$$$\ $$ |          $$ |
#  \_______/  \______/       \__|  \__| \______/   \__|         \__|     \__| \______/ \_______/ \______|\__|          \__|
# Helper function to carry out some type conversions
def load_and_format_run(f1,f2,guess,offset):
    ctext1 = f1.readlines()[0]
    ctext2 = f2.readlines()[0]
    c1bin = binascii.unhexlify(ctext1)
    c2bin = binascii.unhexlify(ctext2)
    assert len(c1bin) == len(c2bin) 
    guessbin = guess.encode('ascii')
    output = task1(c1bin,c2bin,guessbin,offset)
    assert isinstance(output,bytearray)==True,"task1(c1bin,c2bin,guessbin,offset) must return a byte array"
    f = open('task1.out', 'w')
    f.write(str(output.hex()))
    f.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(usage="%(prog)s path/to/ciphertext1.txt path/to/ciphertext2.txt 'a multi word guess' 5")
    parser.add_argument('ciphertext1', help = 'path to file for ciphertext1')
    parser.add_argument('ciphertext2', help = 'path to file for ciphertext2')
    parser.add_argument('guess', help = 'A string. Note to pass in a multi word guess you need to put quotes around it ')
    parser.add_argument('offset', help = 'An integer where guess goes',type=int)
    args = parser.parse_args()
    with open(args.ciphertext1) as f1:
        with open(args.ciphertext2) as f2:
            load_and_format_run(f1,f2,args.guess,args.offset)
