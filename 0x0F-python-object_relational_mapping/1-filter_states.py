#!/usr/bin/python3
''' script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa '''

import sys
import MySQLdb


def main():
    '''main func'''
    if (sys.argv.__len__() != 4):
        return
    _, username, password, dbname = sys.argv

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             password=password, database=dbname)
        cursor = db.cursor()
        cursor.execute(
            """SELECT id, name FROM states
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC""")
    except MySQLdb.MySQLError as exc:
        print("DB Error", exc)

    for row in cursor.fetchall():
        print(row)


if __name__ == '__main__':
    main()
