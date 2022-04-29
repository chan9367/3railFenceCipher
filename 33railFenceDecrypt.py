"""Decrypt a Civil War 'rail fence' type cipher.
This is for a "3-rail" fence cipher for short messages
Example plaintext:  'We are discovered run at once'
Rail fence style:  W   E   C   R   U   O
                     E R D S O E E R N T N E
                      A   I   V   D   A   C
Read zig-zag:      \/\/\/\/\/\/\/\/\/\/
Ciphertext:  WECRUO ERDSOEERNTNE AIVDAC 
"""
import math
import itertools
from pydoc import plain

#------------------------------------------------------------------------------
# USER INPUT:

# the string to be decrypted (paste between quotes):
ciphertext = """WECRUO ERDSOEERNTNE AIVDAC
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------




def main():
    """Run program to decrypt 2-rail rail fence cipher."""
    message = prep_ciphertext(ciphertext)
    row1, row2, row3 = split_rails(message)
    decrypt(row1, row2, row3)
    
def prep_ciphertext(ciphertext):
    """Remove whitespace."""
    message = "".join(ciphertext.split())
    print("\nciphertext = {}".format(ciphertext))
    return message

def split_rails(message):
    """Split message in two, always rounding UP for 1st row.
        N = 3 which is the number of rails
        L is the length of the message, which must be a multiple of 2(N-1) which in this case 
        means L must be a multiple of 4
        K is the length of the first and third rail, which must be L/2(N-1)
        2K is the length of the middle rail
    """
    N = 3
    L = len(message)
    K = int(L/(2*(N-1)))
    
    row_1_len = K
    row_2_len = 3*K
 

    row1 = (message[:row_1_len])
    row2 = (message[row_1_len:row_2_len])
    row3 = (message[row_2_len:])
    
    """Need to pad all the rows into length of message for decryption later"""
    newRow1 = ''
    newRow2 = ''
    newRow3 = '..'

    for letter in row1:
        newRow1 += letter
        newRow1 += '...'

    for letter in row2:
        newRow2 += '.'
        newRow2 += letter

    for letter in row3:
        newRow3 += letter
        newRow3 += '...'
    newRow3 = newRow3[:-2]

    return newRow1, newRow2, newRow3

def decrypt(row1, row2, row3):
    """N = 3 which is the number of rails
        The vertical position repeats in sequence of 4, which is 2(N-1)
        That sequence is used for decrypting the ciphertext rows
    """
    plaintext = []
    N = 3
    Sequence = 2*(N-1)

    """I dont even know how I figured this out, but it works"""
    for i in range(Sequence, len(row1)+Sequence-2):
        plaintext.append(row1[i-Sequence])
        plaintext.append(row2[i+1-Sequence])
        plaintext.append(row3[i+2-Sequence])
    plaintext.append(row2[-1])

    """To remove the periods in the plaintext"""
    for i in range(0,len(plaintext)):
        if plaintext[i] == '.':
            plaintext[i] = ''

    while '#' in plaintext:
        plaintext.pop()
    print("rail 1 = {}".format(row1))
    print("rail 2 = {}".format(row2))
    print("rail 3 = {}".format(row3))
    print("\nplaintext = {}".format(''.join(plaintext)))

if __name__ == '__main__':
    main()