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
INSERT INTO "user"
(ID, AVG_PERIOD_DURATION, AVG_PERIOD_GAP, IS_NOTIFICATION_ENABLED)
VALUES('ag', 0, 0, true)

INSERT INTO "user"
(ID, AVG_PERIOD_DURATION, AVG_PERIOD_GAP, IS_NOTIFICATION_ENABLED)
VALUES('v', 7, 21, true)
""")

conn.commit()
print("Data inserted scuuessfully")

conn.close()