import tkinter as tk
from tkinter import *
from tkinter import messagebox, END
import os
import qrcode
import image


root = tk.Tk()
root.title("Text Box with Submit Button")
root.geometry("600x400")

qr = qrcode.QRCode(version=8.0, error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4)

#New save folder
new_folder = "saved_QRcode"
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

#Text boxes
label = tk.Label(root, text="Please enter Link:")
label.pack(pady=0)

text_box = tk.Entry(root, width=50)
text_box.pack(pady=10)

label = tk.Label(root, text="Please enter file name:")
label.pack(pady=0)

text_box2 = tk.Entry(root, width=50)
text_box2.pack(pady=20)


#submit button
def on_submit():
    qr.add_data(f"{text_box.get()}")
    qr.make(fit=True)
    img = qr.make_image(fill_color="white", back_color="black")
    saved_path = os.path.join(new_folder, f'{text_box2.get()}.png')
    img.save(saved_path)
    qr.clear()
    messagebox.showinfo("Submitted", f"QR code created!")

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=10)

def clear_data():
    text_box.delete(0, tk.END)
    text_box2.delete(0, tk.END)

clear_button = tk.Button(root, text="Clear All", command=clear_data)
clear_button.pack(pady=10)

root.mainloop()