from tkinter import Tk, Label, Entry, Button, Text, END
from Crypto.Cipher import DES
import base64

# Function untuk padding teks agar sesuai dengan blok 8 byte
def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

# Fungsi enkripsi menggunakan DES
def encrypt(plain_text, key):
    des = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted_text = des.encrypt(padded_text.encode('utf-8'))
    return base64.b64encode(encrypted_text).decode('utf-8')

# Fungsi dekripsi menggunakan DES
def decrypt(encrypted_text, key):
    des = DES.new(key, DES.MODE_ECB)
    decoded_encrypted_text = base64.b64decode(encrypted_text)
    decrypted_text = des.decrypt(decoded_encrypted_text).decode('utf-8')
    return decrypted_text.rstrip()

# Fungsi untuk tombol Encrypt
def perform_encryption():
    plain_text = input_text.get("1.0", END).strip()
    key_input = key_entry.get()
    if len(key_input) != 8:
        output_text.delete("1.0", END)
        output_text.insert(END, "Key harus memiliki panjang 8 karakter!")
        return
    key = key_input.encode('utf-8')
    encrypted_text = encrypt(plain_text, key)
    output_text.delete("1.0", END)
    output_text.insert(END, encrypted_text)

# Fungsi untuk tombol Decrypt
def perform_decryption():
    encrypted_text = input_text.get("1.0", END).strip()
    key_input = key_entry.get()
    if len(key_input) != 8:
        output_text.delete("1.0", END)
        output_text.insert(END, "Key harus memiliki panjang 8 karakter!")
        return
    key = key_input.encode('utf-8')
    try:
        decrypted_text = decrypt(encrypted_text, key)
        output_text.delete("1.0", END)
        output_text.insert(END, decrypted_text)
    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"Error: {str(e)}")

# GUI Initialization
root = Tk()
root.title("DES Encryption & Decryption")

# Input Text
Label(root, text="Input Text:").grid(row=0, column=0, padx=10, pady=5)
input_text = Text(root, height=5, width=50)
input_text.grid(row=0, column=1, padx=10, pady=5)

# Key Entry
Label(root, text="Key (8 karakter):").grid(row=1, column=0, padx=10, pady=5)
key_entry = Entry(root, width=50)
key_entry.grid(row=1, column=1, padx=10, pady=5)

# Output Text
Label(root, text="Output Text:").grid(row=2, column=0, padx=10, pady=5)
output_text = Text(root, height=5, width=50)
output_text.grid(row=2, column=1, padx=10, pady=5)

# Buttons
encrypt_button = Button(root, text="Encrypt", command=perform_encryption)
encrypt_button.grid(row=3, column=0, padx=10, pady=5)

decrypt_button = Button(root, text="Decrypt", command=perform_decryption)
decrypt_button.grid(row=3, column=1, padx=10, pady=5)

# Start GUI Loop
root.mainloop()
