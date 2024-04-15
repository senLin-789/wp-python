from faker import Faker

import os
import sys

parentdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(parentdir)

from dao.Database import Database

faker = Faker(locale="zh_CN")


# user
def make_users(len=1):
    rows = []
    for i in range(len):
        rows.append((faker.name(),))
    return rows


def insert_users(rows):
    fields = ("name",)
    dataBase = Database()
    cursor = dataBase.connection.cursor()
    s = ",".join(fields)
    sql = f"insert into user ({s}) values (%s)"
    cursor.executemany(sql, rows)
    dataBase.connection.commit()
    cursor.close()
    print("faker successfully!")


if __name__ == "__main__":
    rows = make_users(100)
    insert_users(rows)
