import tkinter as tk
from tkinter import ttk
import string
import random
from PIL import Image, ImageTk

def generate_password():
    characters = ""
    password_length = length_scale.get()

    if var1.get():
        characters += string.ascii_uppercase
    if var2.get():
        characters += string.ascii_lowercase
    if var3.get():
        characters += string.punctuation
    if var4.get():
        characters += string.digits

    if characters:
        password = ''.join(random.choice(characters) for _ in range(password_length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    else:
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "Veuillez sélectionner au moins une option")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())

def save_to_file():
    file_name = file_name_entry.get()
    if not file_name:
        file_name = "password.txt"
    else:
        if not file_name.endswith('.txt'):
            file_name += '.txt'
    with open(file_name, 'w') as f:
        f.write(password_entry.get())

def set_background(image_path):
    try:
        bg_image = Image.open(image_path)
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(relwidth=1, relheight=1)
    except FileNotFoundError:
        erreur_label = ttk.Label(root, text="Image de fond non trouvée.")
        erreur_label.place(relwidth=1, relheight=1)

root = tk.Tk()
root.title("eliospass")
root.geometry("600x400")
root.iconbitmap('logo.ico')
set_background('bk.png')

var1 = tk.BooleanVar()
var2 = tk.BooleanVar()
var3 = tk.BooleanVar()
var4 = tk.BooleanVar()

length_scale = tk.Scale(root, from_=6, to=20, orient=tk.HORIZONTAL, label="Longueur du mot de passe")
length_scale.pack()

check1 = tk.Checkbutton(root, text="Lettres majuscules (A-Z)", variable=var1)
check1.pack()
check2 = tk.Checkbutton(root, text="Lettres minuscules (a-z)", variable=var2)
check2.pack()
check3 = tk.Checkbutton(root, text="Caractères spéciaux (!,@,#,$, etc.)", variable=var3)
check3.pack()
check4 = tk.Checkbutton(root, text="Chiffres (0-9)", variable=var4)
check4.pack()

generate_button = tk.Button(root, text="Générer un nouveau mot de passe", command=generate_password)
generate_button.pack()

password_entry = tk.Entry(root)
password_entry.pack()

copy_button = tk.Button(root, text="Copier dans le presse-papiers", command=copy_to_clipboard)
copy_button.pack()

# New entry for file name
file_name_label = tk.Label(root, text="Nom du fichier (sans extension) :")
file_name_label.pack()
file_name_entry = tk.Entry(root)
file_name_entry.pack()

save_button = tk.Button(root, text="Enregistrer dans un fichier", command=save_to_file)
save_button.pack()

prevention_text = (
    "La sécurité de vos informations en ligne est cruciale. Un mot de passe fort et unique "
    "est votre première ligne de défense contre les intrusions et les vols d'identité. Il est "
    "recommandé d'utiliser un mélange de lettres majuscules et minuscules, de chiffres et de "
    "caractères spéciaux. N'utilisez jamais d'informations personnelles facilement identifiables "
    "dans vos mots de passe. Changez vos mots de passe régulièrement et n'utilisez jamais le même "
    "mot de passe pour plusieurs comptes."
)
prevention_label = tk.Label(root, text=prevention_text, wraplength=500)
prevention_label.pack()

root.mainloop()
