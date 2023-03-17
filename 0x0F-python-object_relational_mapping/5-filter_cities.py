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
        cursor.execute("""SELECT cities.name
                       FROM states
                       RIGHT JOIN cities ON cities.state_id=states.id
                       WHERE states.name=%s
                       ORDER BY cities.id""",
                       [state])
        res = ", ".join(list(map(lambda x: x[0], cursor.fetchall())))
        print(res)
    except MySQLdb.MySQLError as exc:
        print("DB Error", exc)


if __name__ == '__main__':
    main()
