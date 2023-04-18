import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()

res = cur.execute("SELECT * FROM sicks")
print("----------sicks------------")
for row in res:
    print(row)
print("---------------------------")

res = cur.execute("SELECT * FROM criteria")
print("----------criteria----------")
for row in res:
    print(row)
print("---------------------------")

res = cur.execute("SELECT * FROM criteria_values")
print("------criteria_values-------")
for row in res:
    print(row)
print("---------------------------")


con.close()