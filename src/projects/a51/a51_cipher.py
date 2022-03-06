#!/usr/bin/env python3
"""
A5/1 cipher implementation

@authors: Roman Yasinovskyy
@version: 2022.2
"""

from hashlib import sha256
from pathlib import Path


def populate_registers(init_keyword: str) -> tuple[str, str, str]:
    """Populate registers

    Important: if the keyword is shorted than 8 characters (64 bits),
    pad the resulting short bit string with zeros (0) up to the required 64 bits

    :param init_keyword: initial secret word that will be used to populate registers X, Y, and Z
    :return: registers X, Y, Z as a tuple
    """
    # TODO: Implement this function
    X = ""
    Y = ""
    Z = ""
    
    
    for char in init_keyword:
        X += bin(ord(char))[2:].zfill(8)
        Y += bin(ord(char))[2:].zfill(8)
        Z += bin(ord(char))[2:].zfill(8)
        xyz = str(X+Y+Z)
        
    
    if len(xyz) < 64:
        xyz = xyz.ljust(64,"0")
    
    x = xyz[0:19]
    y = xyz[19:41]
    z = xyz[41:64]
  
    return (x , y, z)


def majority(x8_bit: str, y10_bit: str, z10_bit: str) -> str:
    """Return the majority bit

    :param x8_bit: 9th bit from the X register
    :param y10_bit: 11th bit from the Y register
    :param z10_bit: 11th bit from the Z register
    :return: the value of the majority bit
    """
    # TODO: Implement this function
    if int(x8_bit) + int(y10_bit) + int(z10_bit) > 1:
        return '1'
    else:
        return '0'



def step_x(register: str) -> str:

    """Stepping register X

    :param register: X register
    :return: new value of the X register
    """
    x1 = register[13]
    x2 = register[16]
    x3 = register[17]
    x4 = register[18]
    x_new_first_bit = int(x1) ^ int(x2) ^ int(x3) ^ int(x4) 
    register = str(x_new_first_bit) + register[:18] 

    return register


def step_y(register: str) -> str:

    """Stepping register Y

    :param register: Y register
    :return: new value of the Y register
    """
    y1 = register[20]
    y2 = register[21]
    y_new_first_bit = int(y1) ^ int(y2) 
    register = str(y_new_first_bit) + register[:21] 
    return register


def step_z(register: str) -> str:
    """Stepping register Z

    :param register: Z register
    :return: new value of the Z register
    """
    z1 = register[7]
    z2 = register[20]
    z3 = register[21]
    z4 = register[22]
    z_new_first_bit = int(z1) ^ int(z2) ^ int(z3) ^ int(z4) 
    register = str(z_new_first_bit) + register[:22] 

    return register

def XORedVal(a, b):
    if a != b:
        return "1"
    else:
        return "0"

        
def generate_bit(x: str, y: str, z: str) -> int:

    """Generate a keystream bit

    :param x: X register
    :param y: Y register
    :param z: Z register
    :return: a single keystream bit
    """
    keystream_bit = int(XORedVal(XORedVal(x[18], y[21]), z[22]))
    return keystream_bit
  


def generate_keystream(plaintext: str, x: str, y: str, z: str) -> str:
    """Generate stream of bits to match length of plaintext

    :param plaintext: plaintext to be encrypted
    :param x: X register
    :param y: Y register
    :param z: Z register
    :return: keystream of the same length as the plaintext
    """
    keystream_plaintext = ""
    
    plaintext_binary = ""
    for char in plaintext:
        plaintext_binary += bin(ord(char))[2:].zfill(8)
    
    

    for i in range(0, len(plaintext_binary)):
        maj = majority(x[8], y[10], z[10])
        if x[8] == maj:
            x = step_x(x)
        if y[10] == maj:
            y = step_y(y)
        if z[10] == maj:
            z = step_z(z)

        bit = generate_bit(x, y, z)
        
        keystream_plaintext += str(bit)
    return keystream_plaintext


def encrypt(plaintext: str, keystream: str) -> str:
    """Encrypt plaintext using A5/1

    :param plaintext: plaintext to be encrypted
    :param keystream: keystream
    :return: ciphertext
    """
    ciphertext = ""
    
    plaintext_binary = ""
    for char in plaintext:
        plaintext_binary += bin(ord(char))[2:].zfill(8)    
    
    for i in range(0, len(plaintext_binary)):
        ciphertext += XORedVal(plaintext_binary[i], keystream[i])
    
    return ciphertext
    


def decrypt(ciphertext: str, keystream: str) -> str:
    """Decrypt ciphertext using A5/1

    :param ciphertext: ciphertext to be decrypted
    :param keystream: keystream
    :return: plaintext
    """
    # TODO: Implement this function
    plaintext = ""
    
    plaintext_binary = []  
    i = 0
    while(i < len(cipher)):
        plaintext_binary.insert(i,int(plaintext[i]))
        plaintext += str(XORedVal(plaintext_binary[i], keystream[i]))
        i += 1
    
    return plaintext


def encrypt_file(filename: str, secret: str) -> None:
    """Encrypt a file

    For the sake of output comparison you should preserve end-of-line (\n) symbols
    in the output file.

    :param filename: filename to be encrypted
    :param secret: secret to initialize registers
    :return: write the result to filename.secret
    """
   


def main():

    """Main function"""


if __name__ == "__main__":
    main()
