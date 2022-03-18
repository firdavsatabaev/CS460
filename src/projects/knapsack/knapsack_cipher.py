#!/usr/bin/env python3
"""
Merkle-Hellman Knapsack cipher implementation

@authors: 
@version: 2022.3
"""

import math
import pathlib
import random
import sys

BLOCK_SIZE = 64



def generate_sik(size: int = BLOCK_SIZE) -> tuple[int, ...]:
    """
    Generate a superincreasing knapsack of the specified size

    :param size: block size
    :return: a superincreasing knapsack as a tuple
    """
    # TODO: Implement this function
    knapsackList = []
    sum = 0
    for i in range(size):
        val = random.randrange(sum+1, sum+10)
        knapsackList.append(val)
        sum += val
    
    return tuple(knapsackList)
    


def calculate_n(sik: tuple) -> int:
    """
    Calculate N value

    N is the smallest number greater than the sum of values in the knapsack

    :param sik: a superincreasing knapsack
    :return: n
    """
    # TODO: Implement this function
    sum = 0
    for i in sik:
        sum += i
    n = sum + 1
    return n

def gcd(a ,b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def calculate_m(n: int) -> int:
    """
    Calculate M value

    M is the largest number in the range [1, N) that is co-prime of N
    :param n: N value
    """
    # TODO: Implement this function
    for i in range(n-1, 0, -1):
        if gcd(i, n) == 1:
            return i
        


def calculate_inverse(sik: tuple[int, ...], n: int = None, m: int = None) -> int:
    """
    Calculate inverse modulo

    :param sik: a superincreasing knapsack
    :param n: N value
    :param m: M value
    :return: inverse modulo i so that m*i = 1 mod n
    """
    # TODO: Implement this function
      
    if n == None:
        return sum(sik)
    
    n0 = n 
    y = 0
    x = 1
  
    if (n == 1) : 
        return 0
  
    while (m > 1) : 
  
        q = m // n 
  
        t = n
  
        n = m % n 
        m = t 
        t = y 
  
        y = x - q * y 
        x = t 
  
  
    # Turn the x value into positive in case it is negative
    if (x < 0) : 
        x = x + n0 
  
    return x 


def generate_gk(sik: tuple[int, ...], n: int = None, m: int = None) -> tuple[int, ...]:
    """
    Generate a general knapsack from the provided superincreasing knapsack

    :param sik: a superincreasing knapsack
    :param n: N value
    :param m: M value
    :return: the general knapsack
    """
    # TODO: Implement this function
    if n == None:
        n = calculate_n(sik)
        m = calculate_m( n)
    x = tuple(sik[i]*m%n for i in range(len(sik)))
    return x


def encrypt(
    plaintext: str, gk: tuple[int, ...], block_size: int = BLOCK_SIZE
) -> list[int]:
    """
    Encrypt a message

    :param plaintext: text to encrypt
    :param gk: general knapsack
    :param block_size: size of the encryption block
    :return: encrypted text
    """
    # TODO: Implement this function
    plaintextEncrypt = len(plaintext)
    
    binary_val = ""
    
    for i in range(plaintextEncrypt):
        print(plaintext[i])
        binary_val += format(ord(plaintext[i]), 'b').zfill(8)
    
    
    encryptedText = 0
    
    gk_idx = len(gk) - 1
    bi_idx = len(binary_val) - 1
    print(gk)
    print(gk_idx, bi_idx)
    while gk_idx >=0 and bi_idx >= 0:
        
        if binary_val[bi_idx] == "1":
            encryptedText += gk[gk_idx]
        gk_idx -= 1
        bi_idx -= 1
        
            
    return [encryptedText]

def decrypt(
    ciphertext: list[int],
    sik: tuple[int, ...],
    n: int = None,
    m: int = None,
    block_size: int = BLOCK_SIZE,
) -> str:
    """
    Decrypt a single block
    
    :param ciphertext: text to decrypt
    :param sik: superincreasing knapsack
    :param n: N value
    :param m: M value
    :param block_size: block size
    :return: decrypted string
    """
    # TODO: Implement this function
    decimal_val = ciphertext[0] * calculate_inverse(sik, n, m) % n
    print(decimal_val)
    
    l = len(sik) - 1
    
    decrypted = ""
    while l >= 0 and decimal_val > 0:
        if decimal_val >= sik[l]:
            decrypted = "1" + decrypted
            decimal_val -= sik[l]
        else:
            decrypted = "0" + decrypted
        l -=1
    
    decrypted = int(decrypted,2)
    decrypted = chr(decrypted)
    # decrypted = result.astype("int64")
    return decrypted


def main():
    """
    Main function
    Use your own values to check that functions work as expected
    You still need to rely on tests for proper verification
    """
    print("Hellman-Merkle example")


if __name__ == "__main__":
    main()
