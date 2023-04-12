import itertools
import pytest
import matplotlib.pyplot as plt
from ahpy import ahpy

vehicles = ('Ap-luc(mm)', 'Bach-cau/microL', 'Loai-te-bao-uu-the', 'Glucose (mg/dL)', 'Protein(mg/dL)')
vehicle_pairs = list(itertools.combinations(vehicles, 2))

criterial_values = (1/3, 1/3, 1, 5, 1, 3, 5, 3, 5, 3)
criterial_comparisons = dict(zip(vehicle_pairs, criterial_values))

criterial = ahpy.Compare('Criteria', criterial_comparisons, precision=3)
report = criterial.report(show=True)

sicks = ('binh-thuong', 'viem-mang-nao-cap-do-vi-khuan', 'viem-mang-nao-ban-cap-va-man-tinh',
    'viem-mang-nao-do-giang-mai-cap-tinh', 'viem-nao-tu-mien', 'giang-mai-than-kinh',
    'benh-lyme-trong-CSF', 'ap-xe-nao-hoac-khoi-u', 'nhiem-virus', 'tang-ap-luc-noi-so-nguyen-phat',
    'huyet-khoi-trong-nao', 'u-tuy-song','da-xo-cung','hoi-chung-Guillain-Barre')

sicks_pairs = list(itertools.combinations(sicks, 2))

sicks_values = ()

sicks_comparisons = dict(zip(sicks_pairs, sicks_values))