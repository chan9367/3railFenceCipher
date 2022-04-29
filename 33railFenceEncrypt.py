"""Encrypt a Civil War 'rail fence' type cipher.
This is for a "3-rail" fence cipher for short messages
Example text to encrypt:  'We are discovered run at once'
Rail fence style:   W   E   C   R   U   O
                     E R D S O E E R N T N E
                      A   I   V   D   A   C
Read zig-zag:      \/\/\/\/\/\/\/\/\/\/
Encrypted:  WECRUO ERDSOEERNTNE AIVDAC 
"""
#------------------------------------------------------------------------------
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """We are discovered run at once
"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!
#------------------------------------------------------------------------------

def main():
    """Run program to encrypt message using 2-rail rail fence cipher."""
    message = prep_plaintext(plaintext)
    rails = build_rails(message)
    encrypt(rails)

def prep_plaintext(plaintext):
    """Remove spaces & leading/trailing whitespace & periods."""
    message = "".join(plaintext.split())
    message = "".join(message.split('.'))
    message = message.upper()  # convention for ciphertext is uppercase 
    print("\nplaintext = {}".format(plaintext))
    return message

def build_rails(message):
    """Build strings into 3 rails. 
        N = 3 which is the number of rails
        L is the length of the message, which must be a multiple of 2(N-1) which in this case 
        means L must be a multiple of 4
    """
    N = 3
    L = len(message)
    
    while L%2*(N-1) != 0:
        """"padding the message so it is a multiple of 4"""
        message += '#'
        L = len(message)
    firstRail = message[::4]
    secondRail = message[1::2]
    thirdRail = message[2::4]
    rails = firstRail + secondRail + thirdRail
    return rails

def encrypt(rails):
    """Split letters in ciphertext into chunks of 5 & join to make string.
        N = 3 which is the number of rails
        L is the length of the message, which must be a multiple of 2(N-1) which in this case 
        means L must be a multiple of 4
        K is the length of the first and third rail, which must be L/2(N-1)
        2K is the length of the middle rail
    """
    N = 3
    L = len(rails)
    K = int(L/(2*(N-1)))
    ciphertext = ' '.join([rails[i:i+K] for i in range(0, len(rails), K)]) 
    """concatenate the ciphers to make the middle rail length = 2K"""
    ciphertext = ciphertext[:2*K+1]+ciphertext[2*K+2:]
    print("ciphertext = {}".format(ciphertext))

if __name__ == '__main__':
    main()