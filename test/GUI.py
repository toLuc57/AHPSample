from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Test nhập dữ liệu nồng độ đo về dịch não tuỷ")
window.geometry('410x230')

ap_luc = Label(window, text="Áp lực (mm): ")
ap_luc.grid(column=0, row=0)
txt_ap_luc = Entry(window)
txt_ap_luc.grid(column=1, row=0)

bach_cau = Label(window, text="Bạch cầu/microL: ")
bach_cau.grid(column=0, row=1)
txt_bach_cau = Entry(window)
txt_bach_cau.grid(column=1, row=1)

cm_tb_uu_the = Combobox(window)
cm_tb_uu_the['values']= ("Bạch cầu Lympho (L)", "Bạch cầu đa nhân trung tính (PMN)")
cm_tb_uu_the.grid(column=1, row=2)
cm_tb_uu_the.current(1)
tb_uu_the = Label(window, text="Bạch cầu/microL: ")
tb_uu_the.grid(column=0, row=2)


glucose = Label(window, text="Glucose (mg/dL): ")
glucose.grid(column=0, row=3)
txt_glucose = Entry(window)
txt_glucose.grid(column=1, row=3)

protein = Label(window, text="Protein (mg/dL): ")
protein.grid(column=0, row=4)
txt_protein = Entry(window)
txt_protein.grid(column=1, row=4)

txt_result = Label(window, text="Kết quả: ")
txt_result.grid(column=0,row=6)
txt_result = Label(window, text="")
txt_result.grid(column=1,row=6)

txt_ap_luc.focus()

def clicked():
    ap_luc_nb = float(ap_luc.get())
    bach_cau_nb = float(bach_cau.get())
    tb_uu_the_str = float(tb_uu_the.get())
    glucose_nb = float(glucose.get())
    protein_nb = float(protein.get())
    res = (ap_luc_nb + bach_cau_nb + protein_nb + glucose_nb)/4
    result.configure(text= res)

btn = Button(window, text="Tính toán", command=clicked)
btn.grid(column=1, row=5)

window.mainloop()