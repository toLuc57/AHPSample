import itertools
import pytest
import matplotlib.pyplot as plt
from ahpy import ahpy

trieuchungs = ('Ap-luc', 'Bach-cau/microL', 'Loai-te-bao-uu-the', 'Glucose', 'Protein(mg/dL)')
trieuchung_pairs = list(itertools.combinations(trieuchungs, 2))

criteria_values = (1/9, 1/6, 1/6, 1/7, 4, 3, 3, 2, 1, 1)
criteria_comparisons = dict(zip(trieuchung_pairs, criteria_values))

criteria = ahpy.Compare('Criteria', criteria_comparisons, precision=4)

sicks = ('binh-thuong', 'viem-mang-nao-cap-do-vi-khuan', 
    'viem-mang-nao-ban-cap-va-man-tinh', 'viem-nao-tu-mien')

sicks_pairs = list(itertools.combinations(sicks, 2))

apluc_values = (9, 1.34, 1, 1/9, 1/9, 0.75)
apluc_comparisons = dict(zip(sicks_pairs, apluc_values))
apluc = ahpy.Compare('Ap-luc', apluc_comparisons, precision=4)
print(apluc.consistency_ratio)

bachcau_values =  (9, 9, 2, 1, 1/9, 1/9)
bachcau_comparisons = dict(zip(sicks_pairs, bachcau_values))
bachcau = ahpy.Compare('Bach-cau/microL', bachcau_comparisons, precision=4)
print(bachcau.consistency_ratio)

tbuuthe_values =  (9, 1, 1, 1/9, 1/9, 1)
tbuuthe_comparisons = dict(zip(sicks_pairs, tbuuthe_values))
tbuuthe = ahpy.Compare('Loai-te-bao-uu-the', tbuuthe_comparisons, precision=4)
print(tbuuthe.consistency_ratio)

glucozo_values =  (9, 9, 1, 1, 1/9, 1/9)
glucozo_comparisons = dict(zip(sicks_pairs, glucozo_values))
glucozo = ahpy.Compare('Glucose', glucozo_comparisons, precision=4)
print(glucozo.consistency_ratio)

protein_values =  (9, 9, 1.02, 2/3, 1/9, 0.12)
protein_comparisons = dict(zip(sicks_pairs, protein_values))
protein = ahpy.Compare('Protein(mg/dL)', protein_comparisons, precision=4)
print(protein.consistency_ratio)

criteria.add_children([apluc, bachcau, tbuuthe, glucozo, protein])
criteria.report(show=True)