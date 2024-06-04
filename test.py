# from getpass import getpass
from mysql.connector import connect, Error

try:
    conn = connect(
        host="localhost",
        user='root',
        password='password',
        database="ane_base",
        autocommit=True,
        auth_plugin='mysql_native_password'
    )
    print(conn)
except Error as e:
    print(e)