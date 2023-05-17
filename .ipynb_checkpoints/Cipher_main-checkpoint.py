import tkinter as tk


def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def encrypt_message():
    text = e1.get()
    shift = int(e2.get())
    e3.delete(0, tk.END)
    e3.insert(tk.END, encrypt(text, shift))


def decrypt_message():
    text = e4.get()
    shift = int(e5.get())
    e6.delete(0, tk.END)
    e6.insert(tk.END, decrypt(text, shift))


master = tk.Tk()
master.title("Caesar Cipher")

# Encryption Section
tk.Label(master, text="--- ENCRYPTION ---", font=('Helvetica',
         14, 'bold')).grid(row=0, column=0, columnspan=2)
tk.Label(master, text="Plain Text:").grid(row=1, pady=5)
tk.Label(master, text="Shift:").grid(row=2, pady=5)
tk.Label(master, text="Cipher Text:").grid(row=3, pady=5)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)

e1.grid(row=1, column=1, pady=5)
e2.grid(row=2, column=1, pady=5)
e3.grid(row=3, column=1, pady=5)

# Decryption Section
tk.Label(master, text="--- DECRYPTION ---", font=('Helvetica',
         14, 'bold')).grid(row=4, column=0, columnspan=2, pady=20)
tk.Label(master, text="Cipher Text:").grid(row=5, pady=5)
tk.Label(master, text="Shift:").grid(row=6, pady=5)
tk.Label(master, text="Plain Text:").grid(row=7, pady=5)

e4 = tk.Entry(master)
e5 = tk.Entry(master)
e6 = tk.Entry(master)

e4.grid(row=5, column=1, pady=5)
e5.grid(row=6, column=1, pady=5)
e6.grid(row=7, column=1, pady=5)

# Buttons
tk.Button(master, text='Encrypt', command=encrypt_message).grid(
    row=8, column=0, columnspan=2, pady=20)
tk.Button(master, text='Decrypt', command=decrypt_message).grid(
    row=9, column=0, columnspan=2, pady=20)

master.mainloop()
