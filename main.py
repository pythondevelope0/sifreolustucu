import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def on_generate():
    try:
        length = int(entry.get())
        password = generate_password(length)
        pyperclip.copy(password)
        messagebox.showinfo("Oluşturulan Şifre", f"Oluşturulan şifre: {password}\nŞifre panoya kopyalandı.")
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli bir sayı girin.")

# GUI oluşturma
root = tk.Tk()
root.title("Rastgele Şifre Oluşturucu")
root.geometry("400x200")
root.resizable(False, False)

# Stil ayarları
root.configure(bg="#2c3e50")
style = {
    "bg": "#2c3e50",
    "fg": "#ecf0f1",
    "font": ("Helvetica", 12)
}

tk.Label(root, text="Şifrenizin uzunluğunu girin:", **style).pack(pady=10)
entry = tk.Entry(root, font=("Helvetica", 12))
entry.pack(pady=5)

tk.Button(root, text="Şifre Oluştur", command=on_generate, bg="#e74c3c", fg="#ecf0f1", font=("Helvetica", 12)).pack(pady=20)

root.mainloop()