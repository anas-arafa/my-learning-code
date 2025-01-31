import tkinter as tk
from tkinter import ttk

def encrypt(text):
    encrypted_text = '     '
    for char in text:
        encrypted_text += chr(((ord(char) + 5) * 2) % 256)
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        decrypted_text += chr(int((ord(char) / 2) - 5) % 256)
    return decrypted_text

def encrypt_text():
    input_text = input_entry.get("1.0", tk.END).strip()
    encrypted_text = encrypt(input_text)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", encrypted_text)

def decrypt_text():
    input_text = input_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())
    encrypted_text = input("Enter the encrypted text: ")
    decrypted_text = decrypt(input_text, shift)
    output_entry.delete("1.0", tk.END)
    output_entry.insert("1.0", decrypted_text)

# Create main window
root = tk.Tk()
root.title("أمن المعلومات و(استخدام الأساليب الرياضية في التشفير)\n"
           "by ANAS  TAMER\n"
           "  under supervision  DR/ AMR GHERIEB")

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

shift_label = ttk.Label(decryption_frame, text="Enter shifting process:")
shift_label.pack(padx=5, pady=5)

shift_entry = ttk.Entry(decryption_frame)
shift_entry.pack(padx=5, pady=5)

decrypt_button = ttk.Button(decryption_frame, text="Decrypt", command=decrypt_text)
decrypt_button.pack(padx=5, pady=5)

# Output text
output_label = ttk.Label(root, text="Output:")
output_label.pack(padx=5, pady=5)

output_entry = tk.Text(root, height=5)
output_entry.pack(padx=5, pady=5)

root.mainloop()