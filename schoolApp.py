import tkinter as tk
import string
from tkinter import ttk

def encrypt(text, shift):
    key = int(shift)
    start = ord('a')
    encrypted_text = ''
    for char in text.lower():
        if(char == " "):
            encrypted_text += " "
        elif(not char.isalpha()):
            encrypted_text += char
        else:
            charIndex = string.ascii_lowercase.index(char)
            encrypted_text += chr(((charIndex + key) % 26) + start)
    return encrypted_text

def decrypt(text, shift):
    key = int(shift)
    start = ord('a')
    decrypted_text = ''

    for char in text.lower():
        if (char == " "):
            decrypted_text += " "
        elif (not char.isalpha()):
            decrypted_text += char
        else:
            charIndex = string.ascii_lowercase.index(char)
            decrypted_text += chr(((charIndex - key) % 26) + start)
    return decrypted_text
def encrypt_text():
    input_text = input_entry.get("1.0", tk.END).strip()
    shift = (shift_entry.get())
    encrypted_text = encrypt(input_text, shift)

    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", encrypted_text)

def decrypt_text():
    input_text = input_d_entry.get("1.0", tk.END).strip()
    shift = (shift_entry.get())
    decrypted_text = decrypt(input_text, shift)

    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", decrypted_text)

# Create main window
root = tk.Tk()
root.title("أمن المعلومات و استخدام الأساليب الرياضية في التشفير")

# Create notebook
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create encryption tab
encryption_frame = ttk.Frame(notebook)
notebook.add(encryption_frame, text='Encryption')

input_label = ttk.Label(encryption_frame, text="Enter text to encrypt:")
input_label.pack(padx=5, pady=5)

input_entry = tk.Text(encryption_frame, height=5)
input_entry.pack(padx=5, pady=5)

encrypt_button = ttk.Button(encryption_frame, text="Encrypt", command=encrypt_text)
encrypt_button.pack(padx=5, pady=5)

# Create decryption tab
decryption_frame = ttk.Frame(notebook)
notebook.add(decryption_frame, text='Decryption')

input_d_label = ttk.Label(decryption_frame, text="Enter text to decrypt:")
input_d_label.pack(padx=5, pady=5)

input_d_entry = tk.Text(decryption_frame, height=5)
input_d_entry.pack(padx=5, pady=5)

decrypt_button = ttk.Button(decryption_frame, text="Decrypt", command=decrypt_text)
decrypt_button.pack(padx=5, pady=5)

# key
shift_label = ttk.Label(root, text="shift number from 1 to 25:")
shift_label.pack(padx=5, pady=5)

shift_entry = ttk.Entry(root)
shift_entry.pack(padx=5, pady=5)

# Output text
output_label = ttk.Label(root, text="Output:")
output_label.pack(padx=5, pady=5)

output_entry = tk.Text(root, height=10)
output_entry.pack(padx=5, pady=5)

info_label = ttk.Label(root, text="By ANAS  TAMER YOUSRY\nUnder supervision  DR/ AMR GHERIEB  from AL safwa school  ")
info_label.pack(padx=5, pady=5)

root.mainloop()