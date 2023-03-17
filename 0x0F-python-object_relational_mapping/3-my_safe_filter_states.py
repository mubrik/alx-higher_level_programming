#!/usr/bin/python3
''' script that lists all states with a name starting with N (upper N) from
the database hbtn_0e_0_usa '''

import sys
import MySQLdb


def main():
    '''main func'''
    if (sys.argv.__len__() != 5):
        return
    _, username, password, dbname, state = sys.argv

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             password=password, database=dbname)
        cursor = db.cursor()
        cursor.execute("""SELECT * FROM states
                       WHERE name=%s""", [state])
        for row in cursor.fetchall():
            print(row)
    except MySQLdb.MySQLError as exc:
        print("DB Error", exc)


if __name__ == '__main__':
    main()
