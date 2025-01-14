import os
import psycopg2
from dotenv import load_dotenv
import random

# .env fayldan ma'lumotlarni yuklash
load_dotenv()

# PostgreSQL ulanish sozlamalari
conn = psycopg2.connect(
    host=os.getenv("db_host"),
    database=os.getenv("db_name"),
    user=os.getenv("db_user"),
    password=os.getenv("db_password"),
    port=5432
)

cur = conn.cursor()
print("Databazaga muvaffaqiyatli ulandi")

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Python jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM python")
Python = cur.fetchall()
random.shuffle(Python)
Togri_javoblar_Python = []
for i in Python:
    Togri_javoblar_Python.append(i[-1])

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# C++ jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM c_plyus")
C_plus = cur.fetchall()
random.shuffle(C_plus)
Togri_javoblar_C_plus = []
for i in C_plus:
    Togri_javoblar_C_plus.append(i[-1])

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
# C# jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM c_sharp")
C_sharp = cur.fetchall()
random.shuffle(C_sharp)
Togri_javoblar_C_sharp = []
for i in C_sharp:
    Togri_javoblar_C_sharp.append(i[-1])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# JavaScript jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM java_script")
JavaScript = cur.fetchall()
random.shuffle(JavaScript)
Togri_javoblar_JavaScript = []
for i in JavaScript:
    Togri_javoblar_JavaScript.append(i[-1])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Java jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM java")
Java = cur.fetchall()
random.shuffle(Java)
Togri_javoblar_Java = []
for i in Java:
    Togri_javoblar_Java.append(i[-1])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# TypeScript jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM type_script")
TypeScript = cur.fetchall()
random.shuffle(TypeScript)
Togri_javoblar_TypeScript = []
for i in TypeScript:
    Togri_javoblar_TypeScript.append(i[-1])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Golang jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM golang")
Golang = cur.fetchall()
random.shuffle(Golang)
Togri_javoblar_Golang = []
for i in Golang:
    Togri_javoblar_Golang.append(i[-1])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Kotlin jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM kotlin")
Kotlin = cur.fetchall()
random.shuffle(Kotlin)
Togri_javoblar_Kotlin = []
for i in Kotlin:
    Togri_javoblar_Kotlin.append(i[-1])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////
# PHP jadvalidan ma'lumotlarni olish va aralashtirish
cur.execute("SELECT * FROM php")
PHP = cur.fetchall()
random.shuffle(PHP)
Togri_javoblar_PHP = []
for i in PHP:
    Togri_javoblar_PHP.append(i[-1])

# Baza ulanishini yopish
cur.close()
conn.close()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# // ////////////////////////////////////////////////////////////////////////////////////////////////////////////
# Jadval nomini o'zgartirish uchun oldindan berilgan nom
# table_name = "php"
#
# # Jadvalni yaratish uchun SQL so'rovi
# create_table_query = sql.SQL("""
# CREATE TABLE IF NOT EXISTS {table_name} (
#     id SERIAL PRIMARY KEY,
#     savol TEXT NOT NULL,
#     a_javob TEXT NOT NULL,
#     b_javob TEXT NOT NULL,
#     c_javob TEXT NOT NULL,
#     t_javob TEXT NOT NULL
# );
# """).format(table_name=sql.Identifier(table_name))
#
# table_name = "type_script"
# data = []
# # Ma'lumotlarni qo'shish uchun SQL so'rovi
# insert_query = sql.SQL("""
# INSERT INTO {table_name} (savol, a_javob, b_javob, c_javob, t_javob)
# VALUES (%s, %s, %s, %s, %s)
# """).format(table_name=sql.Identifier(table_name))
#
# # Har bir dictionary ichidagi ma'lumotlarni qo'shish
# for record in data:
#     cur.execute(insert_query, (
#         record["savol"],
#         record["a_javob"],
#         record["b_javob"],
#         record["c_javob"],
#         record["t_javob"]
#     ))
#
# # O'zgarishlarni saqlash
# conn.commit()
#
# print(f"Ma'lumotlar '{table_name}' jadvaliga muvaffaqiyatli qo'shildi!")


# # Cursor va so'rovni bajarish
# cur = conn.cursor()
# cur.execute(create_table_query)
# conn.commit()
# print(f"'{table_name}' jadvali muvaffaqiyatli yaratildi!")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////
