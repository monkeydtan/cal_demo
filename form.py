import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("กรอกชื่อ")
app.geometry("300x200")

# กรอบใหญ่
frame_window = tk.Frame(app)
frame_window.pack(expand=True)

# head
head_title = tk.Label(frame_window,text="Welcome to game")
head_title.grid(row=0,columnspan=2)

# ไอดี
fname = tk.Label(frame_window,text="Username : ")
fname.grid(row=1,column=0)

entry_fname = tk.Entry(frame_window,bd=2)
entry_fname.grid(row=1,column=1)

# รหัสผ่าน
lname = tk.Label(frame_window,text="Password : ")
lname.grid(row=2,column=0)

entry_lname = tk.Entry(frame_window,bd=2,show="*")
entry_lname.grid(row=2,column=1,pady=5)

# ฟังก์ชันการกดปุ่ม login
def user_id():
    str_name = entry_fname.get() # .get คือการรับข้อความจากช่องข้อความ มาเก็บไว้ในตัวแปร ซึ่งชื่อ str_name
    str_pw = entry_lname.get()
    if not str_name or not str_pw:
        messagebox.showerror("พบข้อผิดพลาด","Username หรือ Password ไม่ถูกต้อง")
    else:
        messagebox.showinfo("เข้าสู่ระบบสำเร็จ","Login Successful ! \nWelcome "+str_name)

    
# กรอบย่อยสำหรับปุ่ม
sub_btn_frame = tk.Frame(frame_window)
sub_btn_frame.grid(row=3,column=1)

# ปุ่ม Login
submit_btn = tk.Button(sub_btn_frame,text="Login",command=user_id)
submit_btn.grid(row=0,column=0,sticky="e",padx=(0,10)) # sticky e คือ ชิดขอบขวา / w คือ ชิดขอบซ้าย
# ปุ่ม Register
regis_btn = tk.Button(sub_btn_frame,text="Register") #command คือมันจะไปหน้าใหม่ (เพิ่ม delay)
regis_btn.grid(row=0,column=1)


app.mainloop()