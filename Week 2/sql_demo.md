# SQL Example via Python
The following example uses Python to manipulate a SQLite database via an interactive session. Try it yourself and move to the SQL summary at the end. The focus here is the SQL (commands inside the `c.execute()`) rather than the Python code.

```python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> conn = sqlite3.connect(r'C:\Users\Yu Sun\Documents\Swinburne\Guest\Week 2\demo.db') # Create a database
>>> c = conn.cursor()
>>> c.execute('CREATE TABLE herbs (name text, pinyin text, property text, jingluo text)') # Create a table
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> c.execute("INSERT INTO herbs VALUES ('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃')") # Insert values
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> c.execute("INSERT INTO herbs VALUES ('白芍', 'Shao Yao', '酸', '肝')")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> c.execute("INSERT INTO herbs VALUES ('赤芍', 'Shao Yao', '酸', '肝 心')")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> conn.commit() # Confirm and perform the actions
>>> 
>>> 
>>> c.execute("SELECT * from herbs")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> result = c.fetchall()
>>> 
>>> from pprint import pprint
>>> pprint(result)
[('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃'),
 ('白芍', 'Shao Yao', '酸', '肝'),
 ('赤芍', 'Shao Yao', '酸', '肝 心')]
>>> 
>>> c.execute("SELECT name, property from herbs")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('生石膏', '淡 微寒'), ('白芍', '酸'), ('赤芍', '酸')]
>>> 
>>> c.execute("SELECT * FROM herbs WHERE pinyin='Shao Yao'")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('白芍', 'Shao Yao', '酸', '肝'), ('赤芍', 'Shao Yao', '酸', '肝 心')]
>>> 
>>> 
>>> c.execute("SELECT * FROM herbs LIMIT 2")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃'), ('白芍', 'Shao Yao', '酸', '肝')]
>>> 
>>> c.execute("SELECT pinyin FROM herbs")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('Sheng Shi Gao',), ('Shao Yao',), ('Shao Yao',)]
>>> c.execute("SELECT DISTINCT pinyin FROM herbs")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('Sheng Shi Gao',), ('Shao Yao',)]
>>> 
>>> c.execute("SELECT * FROM herbs ORDER BY pinyin")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('白芍', 'Shao Yao', '酸', '肝'),
 ('赤芍', 'Shao Yao', '酸', '肝 心'),
 ('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃')]
>>> 
>>> c.execute("SELECT * FROM herbs ORDER BY pinyin DESC")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃'),
 ('白芍', 'Shao Yao', '酸', '肝'),
 ('赤芍', 'Shao Yao', '酸', '肝 心')]
>>> 
>>> 
>>> c.execute("UPDATE herbs SET pinyin='Bai Shao' WHERE name='白芍'")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> 
>>> c.execute("SELECT * FROM herbs")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃'),
 ('白芍', 'Bai Shao', '酸', '肝'),
 ('赤芍', 'Shao Yao', '酸', '肝 心')]
>>> 
>>> c.execute("UPDATE herbs SET pinyin='Chi Shao' WHERE name='赤芍'")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> c.execute("SELECT * FROM herbs")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃'),
 ('白芍', 'Bai Shao', '酸', '肝'),
 ('赤芍', 'Chi Shao', '酸', '肝 心')]
>>> 
>>> c.execute("DELETE FROM herbs WHERE name='赤芍'")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> c.execute("SELECT * FROM herbs")
<sqlite3.Cursor object at 0x0000000003062EA0>
>>> pprint(c.fetchall())
[('生石膏', 'Sheng Shi Gao', '淡 微寒', '肺 胃'), ('白芍', 'Bai Shao', '酸', '肝')]
>>> conn.commit()
>>> conn.close() # Close the database
>>> 
```