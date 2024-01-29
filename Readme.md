## Text-Object Basic Cript Project

<p align="center">
  <img src=".github/banner.png">
</p>

TOB is software that allows users to securely and efficiently encrypt and decrypt text. The following is a summary of how this program can work:

- **Key Generation**: The program generates a random cryptographic key that will be used to encrypt and decrypt the data.
- **Encryption**: The user enters the text they want to encrypt into the program, which uses the generated key to transform the text into an encrypted form.
- **Decryption**: When the user wants to access the original text, he enters the encrypted text into the program, which uses the same key to decode the text and return the original text.

This program guarantees protection for your data through a randomly generated 24-digit key. The encryption process adopts Ansi Sliding, where each character of the entered text is transformed into its corresponding ASCII code. It is then added to the final calculation of the entered key, resulting in a transformation for each character. This means that even if someone has access to the encrypted text, it cannot be read without the correct key.

## Installation
### Linux:
```bash
git clone https://github.com/jmktt/tob-cript.git
cd tob-cript
chmod +x installer.sh
sudo ./installer.sh

