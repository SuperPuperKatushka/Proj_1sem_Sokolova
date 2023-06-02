import sqlite3 as sq
from data import turisti_info, turi_info, broni_info
with sq.connect('Turist.db') as con:
    cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS turisti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    pol VARCHAR NOT NULL,
    birthday DATA,
    phone_number VARCHAR,
    email VARCHAR
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS turi (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tur_name VARCHAR NOT NULL,
    country VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    data_start DATA,
    data_end DATA,
    cost DECIMAL
    )""")

cur.execute("""CREATE TABLE IF NOT EXISTS broni (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_turista INTEGER,
    id_tura INTEGER,
    data_broni DATA,
    kolvo_turistov INTEGER,
    FOREIGN KEY (id_turista) REFERENCES turisti(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (id_tura) REFERENCES turi(id) ON DELETE CASCADE ON UPDATE CASCADE
    )""")

with sq.connect('Turist.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO turisti VALUES (? ,? ,? ,? ,? , ?, ?)", turisti_info)

with sq.connect('Turist.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO turi VALUES (?,?,?,?,?,?,?)", turi_info)

with sq.connect('Turist.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO broni VALUES (?,?,?,?,?)", broni_info)

# select 
#1
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from turisti')
#      res = cur.fetchall()
# print(res)
#2
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from turi ORDER BY cost DESC')
#      res = cur.fetchall()
# print(res)
#3
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from broni WHERE id in (SELECT id FROM turi WHERE city="Белек")')
#      res = cur.fetchall()
# print(res)
#4
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from turisti WHERE id in (SELECT id_turista FROM broni WHERE data_broni BETWEEN "2020-11-10" AND "2021-06-30")')
#      res = cur.fetchall()
# print(res)
#5
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT tur_name, country, city from turi')
#      res = cur.fetchall()
# print(res)
#6
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from turisti WHERE pol="Ж" and birthday>"1990-01-01"')
#      res = cur.fetchall()
# print(res)
#7
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from turi WHERE cost>5000')
#      res = cur.fetchall()
# print(res)
#8
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from turisti WHERE id in (SELECT id_turista from broni where id_tura in (SELECT id from turi where tur_name="Крымские достопримечательности"))')
#      res = cur.fetchall()
# print(res)
#9
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * from turisti WHERE id IN (select id_turista from broni where data_broni="2018-03-13")')
#      res = cur.fetchall()
# print(res)
#10
# with sq.connect('Turist.db') as con:
#      cur = con.cursor()
#      cur.execute('SELECT * FROM turisti WHERE phone_number LIKE "+7%"')
#      res = cur.fetchall()
# print(res)

# update
#1
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set data_start="2023-05-01" where id=1')
# #2
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set cost=1500 WHERE id=7')
# #3
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turisti set phone_number="+15551234567" WHERE id=5')
# #4
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE broni SET data_broni="2023-04-05" WHERE id=3')
# #5
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE broni set kolvo_turistov=3 WHERE id=8')
# #6
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set data_end="2023-08-31" WHERE id=2')
# #7
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turisti SET email="new_email@example.com"')
# #8
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set data_start="2023-06-15" WHERE id=4')
# #9
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set data_start="2023-05-01" WHERE country="Испания"')
# #10
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set cost=1500 where tur_name="Греция-отдых на море"')
# #11
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi SET data_start="2023-06-01" WHERE tur_name="Испания-путешествие по городам"')
# #12
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE broni set kolvo_turistov=3 where id=2')
# #13
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turisti set phone_number="+11234567890" where id=2')
# #14
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi SET data_start="2024-07-01" WHERE cost<2000')
# #15
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turisti set email="new_email@example.com" where phone_number like "+7%" or "8%"' )
# #16
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set data_start="2023-08-15" where id in (SELECT id_tura FROM broni WHERE kolvo_turistov>2)')
# #17
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('UPDATE turi set tur_name="Полный отдых на море" where id=3')

#delete
#1
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE id_turista = 1')
#     res = cur.fetchall()
# print(res)
# #2
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE id_turista = 2')
#     res = cur.fetchall()
# print(res)
# #3
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE data_broni = "2022-10-10"')
#     res = cur.fetchall()
# print(res)
# #4
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM turisti WHERE id IN (select id_turista from broni where id_tura=3)')
#     res = cur.fetchall()
# print(res)
# #5
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE id_turista IN (SELECT id FROM turisti where phone_number="89189040467")')
#     res = cur.fetchall()
# print(res)
# #6
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE id_turista IN (SELECT id FROM turisti WHERE email="luceuwoxuzi-3189@yopmail.com")')
#     res = cur.fetchall()
# print(res)
# #7
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE data_broni>"2020-12-11"')
#     res = cur.fetchall()
# print(res)
# #8
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM turisti where id IN (SELECT id_turista FROM broni WHERE id_tura IN (SELECT id FROM turi WHERE country="Турция"))')
#     res = cur.fetchall()
# print(res)
# #9
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE id_tura IN (SELECT id FROM turi WHERE data_end < "2021-03-17")')
#     res = cur.fetchall()
# print(res)
# #10
# with sq.connect('Turist.db') as con:
#     cur = con.cursor()
#     cur.execute('DELETE FROM broni WHERE id_tura IN (SELECT id FROM turi where cost = 4765.55)')
#     res = cur.fetchall()
# print(res)