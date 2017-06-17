"""Variation of aes encryption method for the purposes of the author's learning"""

import sys

def reader():
    """Grabs the filename as passed from the command line
    returns contents as giant string (newlines are lost, oh well)
        """
    filename=sys.argv[-1]
    message=open(filename, "r")

    strversion=""
    for line in message:
        strversion+=line
    return strversion

def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


def encryptor(key, message):
    """the encryption algorithm, should be symmetric
    """
    encrypted=''
    asciied=''

    for letter in message:
        asciied+=str("%03d" % ord(letter))

    partitioned=list(chunkstring(asciied, 6))
    for item in partitioned:
        xor = int(item)^key
        temp=list(chunkstring(str("%06d"% xor),3))
        for cryptlet in temp:
            encrypted+=chr(int(cryptlet))
    return encrypted



def printer(encrypted):
    """Writes the encrypted message to a file. """
    file = open("encryptedMessage.txt","w")
    file.write(encrypted)
    file.close()

if __name__ == '__main__':

    #
    key =

    #extract the file
    message=reader()

    #encrypt
    encrypted=encryptor(key, message)

    #print the encrypted message
    printer(encrypted)
