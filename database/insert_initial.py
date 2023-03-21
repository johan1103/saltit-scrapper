import pymysql.cursors
import pandas as pd

conn = pymysql.connect(
    host='localhost',  # host name
    user='root',  # user name
    password='1234',  # password
    db='saltit_test',  # db name
    charset='utf8'
)


if __name__ == '__main__':
    food_types = ['한식', '양식', '일식', '중식']
    curs = conn.cursor()
    for food in food_types:
        sql = f"insert into food_type(name) values ('{food}')"
        curs.execute(sql)
    select_sql = "select * from food_type"
    curs.execute(select_sql)
    result = curs.fetchall()
    print(type(result))
    for data in result:
        print(data)
    conn.commit()
    conn.close()