# Kode Blue 10/30/2020
# Symmetric key File Encryptor
# FileEncryptor.py

from cryptography.fernet import Fernet
import fleep

def new_key(keyfile):
    """
    Generate New Key, save to file keyfile.key
    """
    keyfile = keyfile + ".key"
    key = Fernet.generate_key()
    with open(keyfile,"wb") as key_file:
        key_file.write(key)
    
    key_file.close()

def load_key(keyfile):
    """
    Load key from file
    """
    return open(keyfile,"rb").read()

def main(keyfile):#,encrypt):
    # Find out if keyfile exists, and is actually a key
    try:
        with open(keyfile,"rb") as file:
            filetype = fleep.get(file.read(128))
            print(filetype.type)
            print(filetype.extension)
            print(filetype.mime)
    except FileNotFoundError:
        filetype = "null"
        pass

    # Open key (or generate new key, then open key)
    #if filetype[1] == 

    #if "encrypt" in encrypt:
        #decrypt the alredy encrypted file
    #else:
    new_key(keyfile)    

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Encrypt a file with a key (saved to a keyfile)")
    parser.add_argument("keyfile", help="File to save key to, or file to read key from. If the script is generating a new key, the .key extention will be appended to the filename you choose.")
#    parser.add_argument("encrypt", help="File to encrypt. Output will be new file *.encrypt")
    # TODO add more encryption schemes, add arguments to use particular scheme

    args = parser.parse_args()
    keyfile = args.keyfile
#    encrypt = args.encrypt

    main(keyfile)#,encrypt)
