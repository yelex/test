# from getpass import getpass
from mysql.connector import connect, Error
import pandas as pd

try:
    conn = connect(
        host="localhost",
        user='root',
        password='password',
        database="ane_base",
        autocommit=True,
        auth_plugin='mysql_native_password'
    )
    df = pd.read_sql(sql = 'select max(date) from parser_app_pricesraw',
                    con=conn)
    print(df)
except Error as e:
    print(e)