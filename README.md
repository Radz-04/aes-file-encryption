# AES File Encryption

A simple Python script to encrypt and decrypt text files using AES in CBC mode.

## What it does
- Encrypts text files using AES (CBC mode)
- Decrypts encrypted files back to original text
- Automated data padding
- Generates a random Initialization Vector (IV) for each encryption

## Requirements
Install `pycryptodome` before running the script:

```bash
pip install pycryptodome
```
## Usage

1. Open `AES.py` and replace the example key and file path with your own:
   ```python
   # Example 
   key = b"ThisIsA16ByteKey"  # Must be 16 bytes
   file_path = r"C:\path\to\your\file.txt"
