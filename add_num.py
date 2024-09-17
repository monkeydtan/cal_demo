import tkinter as tk
from tkinter import messagebox #นำเข้า messagebox

#เพิ่มค่า
def increase():
    global count
    count += 1
    update_label()
    
#ลดค่า
def decrease():
    global count
    if count > 0:
        count -= 1
        update_label()
    else:
        messagebox.showwarning("Warning","ไม่สามารถลดค่าได้มากกว่านี้แล้ว !")
    

# แสดงค่า
def update_label():
    result.config(text=f"ปริมาณ : {count}")
        
    

app = tk.Tk()
app.title("เพิ่ม-ลด-จำนวนตัวเลข")
app.geometry('300x300')
app.configure(background='sky blue')

# ค่าเริ่มต้น
count = 0

# สร้าง Frame
frame = tk.Frame(master=app,background="sky blue")
frame.pack(expand=True)

# head
title_label = tk.Label(frame,text='ปริมาณ',font=20,background='sky blue')
title_label.pack(pady=10)

# frame ของ button
frame_of_btn = tk.Frame(master=frame,background='sky blue')
frame_of_btn.pack(expand=True)

#ปุ่มเพิ่มปริมาณ
btn_up = tk.Button(frame_of_btn,text="\u2191",width=5,font=15,command=increase)
btn_up.pack(side=tk.LEFT,pady=10,padx=5)

#ปุ่มลดปริมาณ
btn_down = tk.Button(frame_of_btn,text="\u2193",width=5,font=15,command=decrease)
btn_down.pack(side=tk.LEFT,pady=10)

#ผลลัพธ์
result = tk.Label(frame,text=f"ปริมาณ : {count}",font=15,background='sky blue')
result.pack(pady=10)



app.mainloop()