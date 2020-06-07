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
DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS "menstrual_cycle";

CREATE TABLE "user"
(
ID VARCHAR(40) PRIMARY KEY NOT NULL,
AVG_PERIOD_DURATION INT DEFAULT 0,
AVG_PERIOD_GAP INT DEFAULT 0,
IS_NOTIFICATION_ENABLED BOOL NOT NULL
);

CREATE TABLE "menstrual_cycle"
(
ID VARCHAR(40) PRIMARY KEY NOT NULL,
PERIOD_BY_MONTH TEXT DEFAULT NULL
);

""")

# period_by_month contains an array of obejects with the following structure:
#   {
    # Period_id varchar(40) NOT NULL,
    # Start_date date default null,
    # Duration int(40) unsigned NOT NULL
# }

conn.commit()
print("Table created scuuessfully")

conn.close()