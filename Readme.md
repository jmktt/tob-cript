## Text-Object Basic Cript Project

<p align="center">
  <img src=".github/banner.png">
</p>

TOB is software that allows users to securely and efficiently encrypt and decrypt text. The following is a summary of how this program can work:

- **Key Generation**: The program generates a random cryptographic key that will be used to encrypt and decrypt the data.
- Encryption: The user enters the text they want to encrypt into the program, which uses the generated key to transform the text into an encrypted form.
- Decryption: When the user wants to access the original text, he enters the encrypted text into the program, which uses the same key to decode the text and return the original text.

This program guarantees protection for your data through a randomly generated 24-digit key. The encryption process adopts Ansi Sliding, where each character of the entered text is transformed into its corresponding ASCII code. It is then added to the final calculation of the entered key, resulting in a transformation for each character. This means that even if someone has access to the encrypted text, it cannot be read without the correct key.

1. **Standard Mode**:
    - Default mode is triggered when no arguments are given when executing the code.
    - It displays an interactive menu in the terminal with the following options:
      - 1- CRYPT: Encrypts a text entered by the user.
      - 2- DECRYPT: Decrypts an encrypted text entered by the user.
      - 3- GEN KEY: Generates a random key.
      - 99- EXIT: Exits the program.

2. **Option `-g` or `--gen-key`**:
    - By supplying the `-g` or `--gen-key` argument when running the code, it generates a random key.
    - The generated key is displayed in the terminal.

3. **Option `-c` or `--crypt`**:
    - By supplying the `-c` or `--crypt` argument followed by a string, you can encrypt the specified string.
    - You also need to supply the `-k` or `--key` argument followed by a key for the encryption.
    - Usage example: `python tob.py -c "text_to_encrypt" -k 12345`

4. **Option `-d` or `--decrypt`**:
    - By supplying the `-d` or `--decript` argument followed by an encrypted text, you can decrypt the specified text.
    - You also need to supply the `-k` or `--key` argument followed by the key corresponding to the encryption.
    - Usage example: `python tob.py -d "encrypted_text" -k 12345`

It is important to provide the correct arguments and in the correct order for each command. Make sure you have Python installed and run the code in a terminal.

## Installation
### Linux:
```bash
git clone https://github.com/jmktt/tob-cript.git
cd tob-cript
chmod +x installer.sh
sudo ./installer.sh

