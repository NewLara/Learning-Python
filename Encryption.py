#Program uses dictionary key:value pairs to encrypt a file and write the encrypted string to another file 
def main():
    #dictionary with values for alphabet and blank space 
    #blank space value is a blank space
    alpha = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '^',
            'F': '&', 'G': '*', 'H':'(', 'I': ')', 'J': '-',
            'K': '+', 'L': '=', 'M': '_', 'N': '?', 'O': '/',
            'P': '>', 'Q': '.', 'R': '<', 'S': ',', 'T': ':',
            'U': ';', 'V': '|', 'W': '!!', 'X': '@@', 'Y': '##', 'Z': '$$', ' ':' '}

    encrypted = openAndReadFile(alpha)
    writeEncryptedToFile(encrypted)

def writeEncryptedToFile(encrypted):
    in_file = open('thisIsEncrypted.txt', 'w')
    in_file.write(encrypted)

def openAndReadFile(alpha):
    #Open file for reading 
    out_file = open('encryptThis.txt', 'r')

    #read out_file contents, 
    encryptedVersion = ''
    for text in out_file:
        #for every character in text see if it is a key in Dictionary
        for ch in text.upper():
            if ch in alpha:
                #store values in encrypted version 
                encryptedVersion += alpha[ch]
    out_file.close()
    return encryptedVersion

main()




   

#use dictionary to encrypt file contents

#close file

#Open file for writing the encrypted contents
#in_file = open('encrypted.py', 'w')


