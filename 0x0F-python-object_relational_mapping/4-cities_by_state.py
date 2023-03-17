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
        cursor.execute("""SELECT cities.id, cities.name, states.name
                       FROM states
                       INNER JOIN cities ON cities.state_id=states.id""")
        for row in cursor.fetchall():
            print(row)
    except MySQLdb.MySQLError as exc:
        print("DB Error", exc)


if __name__ == '__main__':
    main()
