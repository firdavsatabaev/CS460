#!/usr/bin/env python3
"""
Custom VPN. Client

@authors: 
@version: 2022.4
"""
from Crypto.Cipher import AES, DES, Blowfish
from ast import Tuple
from hashlib import sha256

from socket import socket, gethostname, AF_INET, SOCK_STREAM

HOST = gethostname()
PORT = 4600


def generate_cipher_proposal(supported: dict) -> str:
    """Generate a cipher proposal message

    :param supported: cryptosystems supported by the client
    :return: proposal as a string
    """
    
    proposedCipher = "ProposedCiphers:"
    proposedCipher = proposedCipher + ','.join([cipher + ':[' + ','.join([str(x) for x in bits]) + ']'
                     for cipher, bits in supported.items()])

    return proposedCipher

def parse_cipher_selection(msg: str) -> tuple[str, int]:
    """Parse server's response

    :param msg: server's message with the selected cryptosystem
    :return: (cipher_name, key_size) tuple extracted from the message
    """
    ...
    listOfMSG = msg.split(':')[1].split(',')
    cipher_name = listOfMSG[0]
    key_size = int(listOfMSG[1])

    return cipher_name, key_size


def generate_dhm_request(public_key: int) -> str:
    """Generate DHM key exchange request

    :param: client's DHM public key
    :return: string according to the specification
    """
    ...
    return "DHMKE:" + str(public_key)



def parse_dhm_response(msg: str) -> int:
    """Parse server's DHM key exchange request

    :param msg: server's DHMKE message
    :return: number in the server's message
    """
    ...
    result = msg.split(":")
    return int(result[1])
    


def get_key_and_iv(shared_key, cipher_name, key_size):
    """Get key and IV from the generated shared secret key

    :param shared_key: shared key as computed by `diffiehellman`
    :param cipher_name: negotiated cipher's name
    :param key_size: negotiated key size
    :return: (cipher, key, IV) tuple
    cipher_name must be mapped to a Crypto.Cipher object
    `key` is the *first* `key_size` bytes of the `shared_key`
    DES key must be padded to 64 bits with 0
    Length `ivlen` of IV depends on a cipher
    `iv` is the *last* `ivlen` bytes of the shared key
    Both key and IV must be returned as bytes
    """
    ...
    cipher_map = {"DES": DES, "AES": AES, "Blowfish": Blowfish}

    ivlen = {"DES": 8, "AES": 16, "Blowfish": 8}

    selectedCipher = cipher_map.get(cipher_name)
    key = shared_key[:key_size//8]
    if cipher_name == "DES":
        key += '\0'
    key = key.encode()
    iv = shared_key[-1 * ivlen.get(cipher_name):].encode()

    return selectedCipher, key, iv



def add_padding(message: str) -> str:
    """Add padding (0x0) to the message to make its length a multiple of 16

    :param message: message to pad
    :return: padded message
    """
    ...
    padding = len(message)
    while padding % 16 != 0:
        padding += 1
    padding -= len(message)
    paddedMessage = message + '\0' * padding
    return paddedMessage


def encrypt_message(message: str, crypto: object, hashing: object) -> tuple[bytes, str]:
    """
    Encrypt the message

    :param message: plaintext to encrypt
    :param crypto: chosen cipher, must be initialized in the `main`
    :param hashing: hashing object, must be initialized in the `main`
    :return: (ciphertext, hmac) tuple

    1. Pad the message, if necessary
    2. Encrypt using cipher `crypto`
    3. Compute HMAC using `hashing`
    """
    ...
    message = add_padding(message.encode('utf-8'))
    ciphertext = crypto.encrypt(message)
    hashing.update(ciphertext)
    hmcVal = hashing.hexdigest()
    return ciphertext, hmcVal


def main():
    """Main event loop

    See vpn.md for details
    """
    client_sckt = socket(AF_INET, SOCK_STREAM)
    client_sckt.connect((HOST, PORT))
    print(f"Connected to {HOST}:{PORT}")

    print("Negotiating the cipher")
    cipher_name = "CS"
    key_size = 460
    # Follow the description
    print(f"We are going to use {cipher_name}{key_size}")

    print("Negotiating the key")
    # Follow the description
    print("The key has been established")

    print("Initializing cryptosystem")
    # Follow the description
    print("All systems ready")

    while True:
        msg_out = input("Enter message: ")
        if msg_out == "\\quit":
            client_sckt.close()
            break
        client_sckt.send(msg_out.encode())
        msg_in = client_sckt.recv(4096)
        print(msg_in.decode("utf-8"))


if __name__ == "__main__":
    main()
