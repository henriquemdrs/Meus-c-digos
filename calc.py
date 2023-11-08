import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Erro")

def clear():
    entry.delete(0, tk.END)

def delete():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])

def toggle_color(event):
    if button_equal.cget('bg') == 'black':
        button_equal.configure(bg='blue')
    else:
        button_equal.configure(bg='black')

root = tk.Tk()
root.geometry('320x280')
root.title('Calculadora')

canvas = tk.Canvas(root, width=320, height=280, bg='gray')
canvas.pack()

logo_image = tk.PhotoImage(file='logo_ifrn.png').subsample(2, 2)  # Adjust subsample factor as needed
canvas.create_image(10, 10, anchor=tk.NW, image=logo_image)
canvas.create_text(300, 270, text='Lista 12', fill='white', anchor=tk.SE)

entry = tk.Entry(root, font=('Arial', 20), bd=5, justify=tk.RIGHT)
entry.place(x=10, y=50, width=300, height=40)

button_equal = tk.Button(root, text='=', font=('Arial', 20), bg='black', fg='white', command=calculate)
button_equal.place(x=10, y=100, width=75, height=50)
button_equal.bind('<Button-1>', toggle_color)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
]

x, y = 10, 160
button_width, button_height = 75, 50

for button in buttons:
    tk.Button(root, text=button, font=('Arial', 20), command=lambda b=button: entry.insert(tk.END, b)).place(x=x, y=y, width=button_width, height=button_height)
    x += button_width
    if x >= 310:
        x = 10
        y += button_height

clear_button = tk.Button(root, text='C', font=('Arial', 20), command=clear)
clear_button.place(x=10, y=260, width=75, height=50)

delete_button = tk.Button(root, text='←', font=('Arial', 20), command=delete)
delete_button.place(x=85, y=260, width=75, height=50)

root.mainloop()
