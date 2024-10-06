import tkinter as tk
from tkinter import messagebox

def toggle_password():
    if entry_lname.cget('show') == '':
        entry_lname.config(show='*')  # ซ่อนรหัสผ่าน
        eye_canvas.delete("all")
        draw_eye_open()  # วาดไอคอนดวงตาที่เปิดอยู่
    else:
        entry_lname.config(show='')  # แสดงรหัสผ่าน
        eye_canvas.delete("all")
        draw_eye_closed()  # วาดไอคอนดวงตาที่ปิดอยู่

def draw_eye_open():
    # วาดไอคอนดวงตาเปิด
    eye_canvas.create_oval(10, 10, 40, 40, outline='black', fill='white')  # รูปวงกลมตา
    eye_canvas.create_line(10, 25, 40, 25, fill='black', width=2)  # เส้นคิ้ว

def draw_eye_closed():
    # วาดไอคอนดวงตาปิด
    eye_canvas.create_oval(10, 10, 40, 40, outline='black', fill='white')  # รูปวงกลมตา
    eye_canvas.create_line(10, 25, 40, 25, fill='black', width=2)  # เส้นคิ้ว

app = tk.Tk()
app.title("กรอกชื่อ")
app.geometry("300x200")

# กรอบใหญ่
frame_window = tk.Frame(app)
frame_window.pack(expand=True)

# head
head_title = tk.Label(frame_window, text="Welcome to game")
head_title.grid(row=0, columnspan=2, pady=(10, 20))

# ไอดี
fname = tk.Label(frame_window, text="Username : ")
fname.grid(row=1, column=0, padx=10, pady=5)

entry_fname = tk.Entry(frame_window, bd=2)
entry_fname.grid(row=1, column=1, padx=10, pady=5)

# รหัสผ่าน
lname = tk.Label(frame_window, text="Password : ")
lname.grid(row=2, column=0, padx=10, pady=5)

entry_lname = tk.Entry(frame_window, bd=2, show='*')  # เริ่มต้นด้วยการซ่อนรหัสผ่าน
entry_lname.grid(row=2, column=1, padx=10, pady=5)

# กรอบสำหรับไอคอน
eye_canvas = tk.Canvas(frame_window, width=50, height=50, bg='white', bd=0, highlightthickness=0)
eye_canvas.grid(row=2, column=2, padx=5, pady=5)

# วาดไอคอนดวงตาปิด
draw_eye_closed()

# ปุ่มสำหรับสลับการแสดงรหัสผ่าน
eye_btn = tk.Button(frame_window, text="👁", command=toggle_password, bd=0, font=("Arial", 20))
eye_btn.grid(row=2, column=2, padx=5, pady=5)  # ปุ่มที่ใช้เปลี่ยนระหว่างแสดงและซ่อนรหัสผ่าน

app.mainloop()
