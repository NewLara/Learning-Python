#Program uses dictionary key:value pairs to decrypt a file and write the decrypted string screen
def main():
    #dictionary with values for alphabet and blank space ..blank space value is a blank space
    alpha = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '^',
            'F': '&', 'G': '*', 'H':'(', 'I': ')', 'J': '-',
            'K': '+', 'L': '=', 'M': '_', 'N': '?', 'O': '/',
            'P': '>', 'Q': '.', 'R': '<', 'S': ',', 'T': ':',
            'U': ';', 'V': '|', 'W': '[', 'X': '`', 'Y': '~', 'Z': ']', ' ':' '}

    decrypted = openAndReadFile(alpha)
    print(decrypted)
    

def openAndReadFile(alpha):
    #Open file for reading 
    out_file = open('thisIsEncrypted.txt', 'r')

    #read out_file contents, 
    decryptedVersion = ''
    i = 0
    for text in out_file:        
        for ch in text:
            #for every character in text see if it is a key in Dictionary
            for key, value in alpha.items():
                if ch == value:
                    #store values in decrypted version 
                    decryptedVersion += key
                    i += 1
    out_file.close()
    return decryptedVersion

main()



