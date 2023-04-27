import itertools
import pytest
import matplotlib.pyplot as plt
from ahpy import ahpy
import sqlite3
from tkinter import *
from tkinter.ttk import *
import math

def cal_weight(name):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    q = """
    SELECT criteria.name, criteria_values.value FROM criteria_values 
    JOIN criteria on criteria_values.criteria_id = criteria.id
    WHERE sick_id IN (SELECT id FROM sicks WHERE sicks.name = ?)
    """
    res = cur.execute(q,(name,))    
    return res.fetchall()

def set_value_temp(a, b, input):
    if a <= input and input <= b:
        value = max(3, 9*input/(a + b))
    elif a > input:
        value = min(input/a, 1/3)
    elif b < input:
        value = min(b/input, 1/3)
    return value

def set_value(*args):
    result = []
    for arg in args:
        for value in arg:
            a = value[0]
            b = value[1]
            c = min(max(math.floor(a*100/b)/100, 1/9), 9)
            result.append(c)
    return result

trieuchungs = ('Ap-luc', 'Bach-cau/microL', 'Loai-te-bao-uu-the', 'Glucose', 'Protein(mg/dL)')
trieuchung_pairs = list(itertools.combinations(trieuchungs, 2))
criteria_values = (1/9, 1/6, 1/6, 1/7, 4, 3, 3, 2, 1, 1)
criteria_comparisons = dict(zip(trieuchung_pairs, criteria_values))
criteria = ahpy.Compare('Criteria', criteria_comparisons, precision=4)

sicks = ('binh-thuong', 'viem-mang-nao-cap-do-vi-khuan', 
    'viem-mang-nao-ban-cap-va-man-tinh', 'viem-nao-tu-mien')

sicks_pairs = list(itertools.combinations(sicks, 2))

apluc_values_temp = []
bachcau_values_temp = []
tbuuthe_values_temp = []
glucose_values_temp = []
protein_values_temp = []


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
tb_uu_the = Label(window, text="Tế bào ưu thế: ")
tb_uu_the.grid(column=0, row=2)


glucose = Label(window, text="Glucose (mg/dL): ")
glucose.grid(column=0, row=3)
txt_glucose = Entry(window)
txt_glucose.grid(column=1, row=3)

protein = Label(window, text="Protein (mg/dL): ")
protein.grid(column=0, row=4)
txt_protein = Entry(window)
txt_protein.grid(column=1, row=4)

lb_result = Label(window, text="Kết quả: ")
lb_result.grid(column=0,row=6)
txt_result = Label(window, text="")
txt_result.grid(column=1,row=6)

txt_ap_luc.focus()

def clicked():
    ap_luc_nb = int(txt_ap_luc.get())
    bach_cau_nb = int(txt_bach_cau.get())
    tb_uu_the_str = "L"
    if cm_tb_uu_the.current() != "Bạch cầu Lympho (L)": 
        tb_uu_the_str = "PMN"
    glucose_nb = int(txt_glucose.get())
    protein_nb = int(txt_protein.get())
    input = [ap_luc_nb, bach_cau_nb, tb_uu_the_str, glucose_nb, protein_nb]
    
    for sick in sicks:
        criterias = cal_weight(sick)
        apluc_from_to = criterias[0][1].split("-")
        apluc_values_temp.append(set_value_temp(float(apluc_from_to[0]),float(apluc_from_to[1]),input[0]))

        bachcau_from_to = criterias[1][1].split("-")
        bachcau_values_temp.append(set_value_temp(float(bachcau_from_to[0]),float(bachcau_from_to[1]),input[1]))

        if input[2] == criterias[2][1]:
            tbuuthe_values_temp.append(5)
        else:
            tbuuthe_values_temp.append(1/5)

        glucose_from_to = criterias[3][1].split("-")
        glucose_values_temp.append(set_value_temp(float(glucose_from_to[0]),float(glucose_from_to[1]),input[3]))

        protein_from_to = criterias[4][1].split("-")
        protein_values_temp.append(set_value_temp(float(protein_from_to[0]),float(protein_from_to[1]),input[4]))

    apluc_values_temp_pairs = list(itertools.combinations(apluc_values_temp, 2))
    bachcau_values_temp_pairs = list(itertools.combinations(bachcau_values_temp, 2))
    tbuuthe_values_temp_pairs = list(itertools.combinations(tbuuthe_values_temp, 2))
    glucose_values_temp_pairs = list(itertools.combinations(glucose_values_temp, 2))
    protein_values_temp_pairs = list(itertools.combinations(protein_values_temp, 2))

    apluc_values = set_value(apluc_values_temp_pairs)
    bachcau_values = set_value(bachcau_values_temp_pairs)
    tbuuthe_values = set_value(tbuuthe_values_temp_pairs)
    glucose_values = set_value(glucose_values_temp_pairs)
    protein_values = set_value(protein_values_temp_pairs)

    apluc_comparisons = dict(zip(sicks_pairs, apluc_values))
    apluc = ahpy.Compare('Ap-luc', apluc_comparisons, precision=4)

    bachcau_comparisons = dict(zip(sicks_pairs, bachcau_values))
    bachcau = ahpy.Compare('Bach-cau/microL', bachcau_comparisons, precision=4)
    print(bachcau.consistency_ratio)

    tbuuthe_comparisons = dict(zip(sicks_pairs, tbuuthe_values))
    tbuuthe = ahpy.Compare('Loai-te-bao-uu-the', tbuuthe_comparisons, precision=4)
    print(tbuuthe.consistency_ratio)

    glucose_comparisons = dict(zip(sicks_pairs, glucose_values))
    glucose = ahpy.Compare('Glucose', glucose_comparisons, precision=4)
    print(glucose.consistency_ratio)

    protein_comparisons = dict(zip(sicks_pairs, protein_values))
    protein = ahpy.Compare('Protein(mg/dL)', protein_comparisons, precision=4)
    print(protein.consistency_ratio)

    criteria.add_children([apluc, bachcau, tbuuthe, glucose, protein])
    res = criteria.target_weights

    txt_result.configure(text= res)

btn = Button(window, text="Tính toán", command=clicked)
btn.grid(column=1, row=5)

window.mainloop()

