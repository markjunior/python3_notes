sqlite3
```
.help
.tables
.open dog_db.db
CREATE TABLE dogs (name TEXT, breed TEXT, age INTEGER);
INSERT INTO dogs (name, breed, age) VALUES ('blue', 'fold', 3);
SELECT * FROM dogs;
.schema dogs

>>sqlite3 dog_db.db

.read xxx.sql
SELECT * FROM dogs WHERE age > 30 AND breed IS NOT 'ADS' ORDERED BY age;
SELECT * FROM dogs WHERE name LIKE "%gg%";
```

python code
```
import sqlite3
conn = sqlite3.connect('my_friend.db')
#create cursor object
c = conn.cursor()
# execute sql
c.execute("CREATE TABLE dogs (name TEXT, breed TEXT, age INTEGER);")
c.executemany("COMMAND", list_of_tuples)

c.execute("SELECT * FROM dogs")
print(c.fetchall())  #fetch all results as list
print(c.fetchone())

# commit changes
conn.commit()

conn.close()
```
