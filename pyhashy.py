# Importing required libraries
from hashlib import md5, sha256
from argparse import ArgumentParser

# Setting up arguments
parser = ArgumentParser()
parser.add_argument("-m", "--mode", help="Hashing algorythm (sha256, md5)", required=True)
parser.add_argument("-s", "--string", help="String to encrypt", required=True)
args = parser.parse_args()

# SHA-256 encryption
def encrypt_sha256(string):
    sha_signature = \
        sha256(string.encode()).hexdigest()
    return sha_signature

# MD5 encryption
def encrypt_md5(string):
    sha_signature = \
        md5(string.encode()).hexdigest()
    return sha_signature

# Getting arguments
string = args.string
algorythm = args.mode.lower()

# Encrypting based on user's preferred algorythm
if algorythm == "sha256":
    sha256 = encrypt_sha256(string)
    print(sha256)
elif algorythm == "md5":
    md5 = encrypt_md5(string)
    print(md5)