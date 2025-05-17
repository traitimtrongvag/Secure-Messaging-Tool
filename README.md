# Secure-Messaging-Tool
---

This is a **basic Python-based secure messaging tool** that demonstrates how to encrypt and decrypt text using **RSA public-key cryptography**. The tool allows users to generate RSA key pairs, encrypt ("lock") messages with the public key, and decrypt ("unlock") them with the private key.

> **Note:** This tool is designed for educational purposes only and does not include advanced security features required for production use.

---

## Features

- Generate a new RSA key pair (2048-bit)
- Encrypt (lock) a message using the public key
- Decrypt (unlock) a message using the private key
- Base64 encoding for safe message display and transfer
- Simple terminal-based user interface

---

## Prerequisites

- Python 3.6+
- [cryptography](https://pypi.org/project/cryptography/) library

Install the required library using pip:

```bash
pip install cryptography


---

How to Use

1. Run the program:



python rsa_messenger.py

2. Choose an option from the menu:

1: Generate a new RSA key pair

2: Lock (encrypt) a message using the public key

3: Unlock (decrypt) a message using the private key

4: Exit



3. Keys will be saved as:

public.pem – Public Key

secret.pem – Private Key





---

Example Usage

1. Generate Keys

=== CREATE NEW KEYS ===
>> New keys created successfully.

2. Lock Message

=== LOCK MESSAGE ===
Message to lock: Hello, world!

Locked message:
------------------------------
<base64 encoded string>
------------------------------

3. Unlock Message

=== UNLOCK MESSAGE ===
Locked message: <paste base64 string>

Original message:
------------------------------
Hello, world!
------------------------------


---

Limitations

RSA can only encrypt short messages (~200 bytes max with 2048-bit keys).

This tool does not implement hybrid encryption or digital signatures.

Key files are stored in plain PEM format (no password protection).

No network transmission or chat interface is included.



---

Educational Goals

This project was built to help beginners understand the basics of:

Public and private key usage

RSA encryption with OAEP padding

Key generation and storage in PEM format

Secure message handling and base64 encoding



---

License

This project is released under the MIT License. See LICENSE for more details.


---

Date: May 2025

---
