#!/usr/bin/env python3
"""
Custom VPN. Server

@authors: 
@version: 2022.4
"""


from Crypto.Cipher import AES, DES, Blowfish

from socket import socket, gethostname
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

HOST = gethostname()
PORT = 4600


def parse_proposal(msg: str) -> dict[str, list]:
    """Parse client's proposal

    :param msg: message from the client with a proposal (ciphers and key sizes)
    :return: the ciphers and keys as a dictionary
    """
    # TODO: Implement this function
    ...
    current_cipher = ""
    ciphers = msg[16:]
    next = False
    count = 0

    for i in range(len(ciphers)):
        if next == True:
            next = False
            if count == 1:
                current_cipher = ciphers[:i] + ";" + ciphers[i+1:]
            else:
                current_cipher = current_cipher[:i] + ";" + current_cipher[i+1:] 
        else:
            if ciphers[i] == "]":
                next = True
                count += 1
 
    result = current_cipher.split(";")

    for i in range(len(result)):
        result[i] = result[i].split(":")
        result[i][1] = result[i][1].strip("][").split(",")

    
    for m in range(len(result)):
        for n in range(len(result[m][1])):
            result[m][1][n] = int(result[m][1][n].strip())
    print("RESULT", result)

    dictionary = {}
    for i in range(len(result)):
        dictionary[result[i][0]] = result[i][1] 
    print(dictionary)
    return dictionary


def select_cipher(supported: dict, proposed: dict) -> tuple[str, int]:
    """Select a cipher to use

    :param supported: dictionary of ciphers supported by the server
    :param proposed: dictionary of ciphers proposed by the client
    :return: tuple (cipher, key_size) of the common cipher where key_size is the longest supported by both
    :raise: ValueError if there is no (cipher, key_size) combination that both client and server support
    """
    # TODO: Implement this function
    ...
    longest_key_size = 0
    result = ("None",0)
    for key in proposed:
        if key in supported:
            keysize_server = supported[key]
            keysize_client = proposed[key]
            for keysize in keysize_server:
                if keysize in keysize_client and keysize > longest_key_size:
                    result = (key, keysize)

    if result == ("None", 0):
        raise ValueError('there is no (cipher, key_size) combination that both client and server support')
    return result
                


def generate_cipher_response(cipher: str, key_size: int) -> str:
    """Generate a response message

    :param cipher: chosen cipher
    :param key_size: chosen key size
    :return: (cipher, key_size) selection as a string
    """
    # TODO: Implement this function
    ...
    return "ChosenCipher:" + cipher + ":" + str(key_size)


def parse_dhm_request(msg: str) -> int:
    """Parse client's DHM key exchange request

    :param msg: client's DHMKE initial message
    :return: number in the client's message
    """
    # TODO: Implement this function
    ...
    
    result = msg.split(":")

    return int(result[1])


def get_key_and_iv(
    shared_key: str, cipher_name: str, key_size: int
) -> tuple[object, bytes, bytes]:
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
    # TODO: Implement this function
    ...
    byte_shared_key = bytes(shared_key, 'utf-8')
    
    # key
    key = byte_shared_key[:key_size]

    # IV 
    if cipher_name == "AES":
        ivlen = AES.block_size
    elif cipher_name == "DES":
        ivlen = DES.block_size
    else:
        ivlen = Blowfish.block_size
    IV = byte_shared_key[-ivlen:]

    if cipher_name == "AES":
        obj = AES.new(key, AES.MODE_CBC, IV)
    elif cipher_name == "DES":
        obj = AES.new(key, DES.MODE_CBC, IV)
    else:
        obj = AES.new(key, Blowfish.MODE_CBC, IV)
    
    return (obj, key, IV)


def generate_dhm_response(public_key: int) -> str:
    """Generate DHM key exchange response

    :param public_key: public portion of the DHMKE
    :return: string according to the specification
    """
    # TODO: Implement this function
    ...
    return "DHMKE:" + str(public_key)


def read_message(msg_cipher: bytes, crypto: object) -> tuple[str, str]:
    """Read the incoming encrypted message

    :param msg_cipher: encrypted message from the socket
    :crypto: chosen cipher, must be initialized in the `main`
    :return: (plaintext, hmac) tuple
    """
    # TODO: Implement this function
    ...


def validate_hmac(msg_cipher: bytes, hmac_in: str, hashing: object) -> bool:
    """Validate HMAC

    :param msg_cipher: encrypted message from the socket
    :param hmac_in: HMAC received from the client
    :param hashing: hashing object, must be initialized in the `main`
    :raise: ValueError is HMAC is invalid
    """
    # TODO: Implement this function
    ...


def main():
    """Main loop

    See vpn.md for details
    """
    server_sckt = socket(AF_INET, SOCK_STREAM)
    server_sckt.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_sckt.bind((HOST, PORT))
    server_sckt.listen()
    print(f"Listening on {HOST}:{PORT}")
    conn, client = server_sckt.accept()
    print(f"New client: {client[0]}:{client[1]}")

    print("Negotiating the cipher")
    cipher_name = "CS"
    key_size = 460
    # TODO: Follow the description
    print(f"We are going to use {cipher_name}{key_size}")

    print("Negotiating the key")
    # TODO: Follow the description
    print("The key has been established")

    print("Initializing cryptosystem")
    # TODO: Follow the description
    print("All systems ready")

    while True:
        msg_in = conn.recv(4096).decode("utf-8")
        if len(msg_in) < 1:
            conn.close()
            break
        print(f"Received: {msg_in}")
        msg_out = f"Server says: {msg_in[::-1]}"
        conn.send(msg_out.encode())


if __name__ == "__main__":
    main()
