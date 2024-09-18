import tkinter as tk
from tkinter import messagebox

app = tk.Tk()
app.title("กรอกชื่อ")
app.geometry("300x200")

# กรอบใหญ่
frame_window = tk.Frame(app)
frame_window.pack(expand=True)

#กรอบชื่อและช่องกรอก และปุ่ม
fname = tk.Label(frame_window,text="Name : ")
fname.grid(row=0,column=0)

entry_fname = tk.Entry(frame_window,bd=2)
entry_fname.grid(row=0,column=1)

#ฟังก์ชันการกดปุ่ม submit
def save_data():
    str_name = entry_fname.get() # .get คือการรับข้อความจากช่องข้อความ มาเก็บไว้ในตัวแปร ซึ่งชื่อ str_name
    messagebox.showinfo("บันทึกข้อมูล","Name : "+str_name)

#ปุ่ม submit
submit_btn = tk.Button(frame_window,text="Submit",command=save_data)
submit_btn.grid(row=1,columnspan=2,pady=10)



app.mainloop()