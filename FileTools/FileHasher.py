# Kode Blue, 10/30/2020
# Hash an input file

import hashlib

def md5(filename,BLOCKSIZE=65535):
    hash = hashlib.md5()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCKSIZE)
        hash.update(buffer)
    return(hash.hexdigest())

def sha256(filename,BLOCKSIZE=65536):
    hash = hashlib.sha256()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCKSIZE)
        hash.update(buffer)
    return(hash.hexdigest())

def sha512(filename,BLOCKSIZE=65536):
    hash = hashlib.sha512()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCKSIZE)
        hash.update(buffer)
    return(hash.hexdigest())

def blake2s(filename,BLOCKSIZE=65536):
    hash = hashlib.blake2s()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCKSIZE)
        hash.update(buffer)
    return(hash.hexdigest())

def blake2b(filename,BLOCKSIZE=65536):
    hash = hashlib.blake2b()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCKSIZE)
        hash.update(buffer)
    return(hash.hexdigest())

def sha1(filename,BLOCKSIZE=65536):
    hash = hashlib.sha1()
    with open(filename, 'rb') as file:
        buffer = file.read(BLOCKSIZE)
        hash.update(buffer)
    return(hash.hexdigest())

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Get Hash of an input File")
    parser.add_argument("file", help = "File to hash")
    parser.add_argument("algorithm", help = "hashing algorithm to use: [sha1|sha256|sha512|blake2s|blake2b|md5]")
    
    args = parser.parse_args()

    result = locals()[args.algorithm](args.file)
    print(result)
