import psycopg2

DB_NAME = "eidavoeh"
DB_USER = "eidavoeh"
DB_PASS = "85huOjponZ7xudQIVPL3G5D7hcJFHe5C"
DB_HOST = "ruby.db.elephantsql.com"
DB_PORT = "5432"


conn = psycopg2.connect(
        host = DB_HOST,
        database = DB_NAME,
        user = DB_USER,
        port = DB_PORT,
        password = DB_PASS
    )

print("DB connected")

cur = conn.cursor()
cur.execute("""

CREATE TABLE "User"
(
ID VARCHAR(40) PRIMARY KEY NOT NULL,
START_DATE DATE NOT NULL,
DURATION INT NOT NULL,
CREATED_DATE DATE NOT NULL
)

""")

conn.commit()
print("table created scuuessfully")

conn.close()