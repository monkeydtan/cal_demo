import tkinter as tk

def print_something(text):
    print(text)
    

app = tk.Tk()
app.title('โปรแกรมทดลองคลิก')
app.geometry('300x300')
app.configure(background='gray')

btn = tk.Button(text="Click me!",command= lambda :print_something("Print this!"))
btn.pack(pady=10)


app.mainloop()

# import tkinter as tk

# app = tk.Tk()
# app.title("ปุ่มในแนวนอน")
# app.geometry('300x200')
# app.configure(background='sky blue')

# # ปุ่มแรก
# button1 = tk.Button(app, text="ปุ่ม 1", font=20)
# button1.pack(side=tk.LEFT, padx=10, pady=20)

# # ปุ่มที่สอง
# button2 = tk.Button(app, text="ปุ่ม 2", font=20)
# button2.pack(side=tk.LEFT, padx=10, pady=20)

# app.mainloop()

# import tkinter as tk

# app = tk.Tk()
# app.title("ปุ่มในแนวนอน")
# app.geometry('300x200')
# app.configure(background='sky blue')

# # ปุ่มแรก
# button1 = tk.Button(app, text="ปุ่ม 1", font=20)
# button1.grid(row=0, column=0, padx=10, pady=20)

# # ปุ่มที่สอง
# button2 = tk.Button(app, text="ปุ่ม 2", font=20)
# button2.grid(row=0, column=1, padx=10, pady=20)

# app.mainloop()

