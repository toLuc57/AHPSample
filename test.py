import itertools
import pytest
import matplotlib.pyplot as plt
from ahpy import ahpy
import sqlite3

def cal_weight(vehicle):
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    q = """
    SELECT criteria.name, criteria_values.value FROM criteria_values 
    JOIN criteria on criteria_values.criteria_id = criteria.id
    WHERE sick_id IN (SELECT id FROM sicks WHERE sicks.name = ?)
    """
    res = cur.execute(q,(vehicle,))    
    return res.fetchall()

vehicles = ('Bình thường', 'Viêm màng não cấp do vi khuẩn', 'Viêm màng não bán cấp và mạn tính', 'Viêm não tự miễn')
vehicle_pairs = list(itertools.combinations(vehicles, 2))

for vehicle in vehicles:
    print(vehicle + " : ")
    print(cal_weight(vehicle))