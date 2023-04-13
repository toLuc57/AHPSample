import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
# ('sicks',)

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None
# True
cur.execute("CREATE TABLE sicks(id, name)")

data = [(1, 'Bình thường' ),
        (2, 'Viêm màng não bán cấp và mạn tính'),
        (3, 'Viêm não tự miễn')
]

cur.executemany("INSERT INTO sicks VALUES (?,?)", data)
con.commit()

cur.execute("CREATE TABLE criteria(id, name)")

data = [(1, 'Áp lực (mm)' ),
        (2, 'Bạch cầu/microL'),
        (3, 'Loại tế bào ưu thế'),
        (4, 'Glucose ( mg/dL)'),
        (5, 'Protein (mg/dL)')
]

cur.executemany("INSERT INTO criteria VALUES (?,?)", data)
con.commit()

cur.execute("CREATE TABLE criteria_values(id, sick_id, criteria_id, value)")
data = [(1, 1, 1, '100-200'),
        (2, 1, 2, '0-3'),
        (3, 1, 3, 'L'),
        (4, 1, 4, '50-100'),
        (5, 1, 5, '20-45'),
        (6, 2, 1, '200-300'),
        (7, 2, 2, '100-700'),
        (8, 2, 3, 'PMN'),
        (9, 2, 4, '0-50'),
        (10, 2, 5, '100-1000'),
        (11, 3, 1, '100-200'),
        (12, 3, 2, '0-2000'),
        (13, 3, 3, 'L'),
        (14, 3, 4, '50-100'),
        (15, 3, 5, '20-1000'),
]

con.close()