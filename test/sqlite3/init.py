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

con.close()