# Kode Blue, 10/30/2020
# Verify the integrity of a file against a knowable hash
# IntegrityChecker.py

import FileHasher

calls = {"md5":FileHasher.md5,"sha512":FileHasher.sha512,"sha256":FileHasher.sha256,
    "sha1":FileHasher.sha1,"blake2s":FileHasher.blake2s,"blake2b":FileHasher.blake2b}

def depreciated(hash1,hash2=""):
    print(hash1)
    
    if hash2 != "":
        print(hash2)
        if hash1 == hash2:
            print("Looks good. Hashes match!")
        else:
            print("Houston, we have a problem. The hash you gave me isn't the same as the hash of the file")

def main(hash1,hash2):
    print(hash1)
    print(hash2)
    if hash1 == hash2:
        print("Looks good. Hashes match!")
    else:
        print("Houston, we have a problem. These two hashs don't match.")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Compare the Hash of a file against a given hash")
    parser.add_argument("original", help = "Original File")
    parser.add_argument("clone", help = "Cloned File to check")
    parser.add_argument("-a", "--algorithm", help = "Algorithm to use. Default=md5", default = "md5")
    parser.add_argument("--hash", help = "Hash of the file you wish to check", default = "null")

    args = parser.parse_args()
    
    hash1 = calls[args.algorithm](args.original)
    hash2 = calls[args.algorithm](args.clone)
    if args.hash == "null":
        main(hash1,hash2)
    else:
        main(hash1,hash2,args.hash)
