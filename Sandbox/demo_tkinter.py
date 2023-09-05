import tkinter as tk

root = tk.Tk()

root.title('My tkinter demo')
root.configure(bg='#B1D4E0')
root.geometry('500x400+200+200')


def handle_click():
    original_text = original.get('1.0', tk.END).strip()
    encrypted_text = original_text.upper()

    print(f'Original {original_text} => Encrypted {encrypted_text}')

    encrypted.delete('1.0', tk.END)
    encrypted.insert('1.0', encrypted_text)


label1 = tk.Label(root, text = 'Original', bg='#B1D4E0', font = ("Helvetica", 24))
label1.pack(pady = (10, 0))

original = tk.Text(root, height = 5)
original.pack(padx = 10, pady = (0, 10))

button = tk.Button(root, height = 3, width = 10, text = 'Encrypt', font = ("Helvetica", 18), command = handle_click)
button.pack(pady = 20)

label2 = tk.Label(root, text = 'Encrypted', bg='#B1D4E0', font = ("Helvetica", 24))
label2.pack(pady = (10, 0))

encrypted = tk.Text(root, height = 5)
encrypted.pack(padx = 10, pady = (0, 10))

root.mainloop()
