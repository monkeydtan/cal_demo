import tkinter as tk

def on_enter(event):
    label.config(font=('Arial', 16, 'underline'))

def on_leave(event):
    label.config(font=('Arial', 16))

def on_click(event):
    print("Label clicked!")

app = tk.Tk()
app.title("Clickable Label")
app.geometry("300x200")

label = tk.Label(app, text="Click me", font=('Arial', 16), fg='blue', cursor='hand2')
label.pack(pady=20)

label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)
label.bind("<Button-1>", on_click)  # Detect left click

app.mainloop()
