# PyHashy

An easily integratable and lightweight program to turn your strings into hashes!

## Installation

#### Clone the repository
```
git clone https://github.com/cevxl/pyhashy.git
```
#### Change the working directory to pyhashy
```
cd pyhashy
```
and you're done! That's it! It wasn't that hard, was it?

## Usage

Template: `py -m pyhashy.py -m MODE -s STRING`

### Examples:
`py -m pyhashy -m sha256 -s very-secret-text` will encrypt "very-secret-text" in the SHA256 algorythm, and it will print:
14067d2a7b59d74942a10588b969e96aa60b57a620d6c7a3bdfc1ea05809d765

`py -m pyhashy -m md5 -s another-secret-text` will encrypt "another-secret-text" in the MD5 algorythm, and it will print:
c04c167fda80d19fdab227af716b7962

Note: If you ever get stuck, type `py -m pyhashy -h`

If you are using linux, or the commands above don't work, try using python3 instead of py. Example: `py -m pyhashy.py -m MODE -s STRING`
