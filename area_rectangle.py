import tkinter as tk

def cal_Rectangle():
    number_width = int(w_entry.get()) 
    number_height = int(l_entry.get())
    output = f"ผลลัพธ์ : {number_width*number_height}"
    output_rec.configure(text=output) 
    

window = tk.Tk()
window.title('โปรแกรมคำนวณพื้นที่')
window.minsize(width=400,height=400)

title_label = tk.Label(master=window,text='คำนวณหาพื้นที่')
title_label.grid(row=0,column=1,padx=10,pady=5)

# กว้าง
w_input = tk.Label(master=window,text="กว้าง")
w_input.grid(row=1,column=0,padx=0,pady=5)

w_entry = tk.Entry(master=window)
w_entry.grid(row=1,column=1,padx=10,pady=5)

# ยาว
l_input = tk.Label(master=window,text="ยาว")
l_input.grid(row=2,column=0,padx=0,pady=5)

l_entry = tk.Entry(master=window)
l_entry.grid(row=2,column=1,padx=10,pady=5)

# สูง
# h_input = tk.Label(master=window,text="สูง")
# h_input.grid(row=3,column=0,padx=0,pady=5)

# h_entry = tk.Entry(master=window)
# h_entry.grid(row=3,column=1,padx=10,pady=5)

cal_btn = tk.Button(master=window,text="คำนวณ",command=cal_Rectangle)
cal_btn.grid(row=4,column=1,pady=10)

output_rec = tk.Label(master=window)
output_rec.grid(row=5,column=1,padx=10,pady=5)

window.mainloop()