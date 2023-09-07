import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user="postgres",
    password= "$$Dut010107",
    host="localhost",
    port="5432",
)

conn.autocommit = True

cursor_obj = conn.cursor()
cursor_obj.execute('''CREATE DATABASE dcrm''')

print('All done')