# Getting Started

Install mySQL and add cats table: https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing

cats table description:

```
+-------+--------------+------+-----+---------+----------------+
| Field | Type         | Null | Key | Default | Extra          |
+-------+--------------+------+-----+---------+----------------+
| id    | int unsigned | NO   | PRI | NULL    | auto_increment |
| name  | varchar(150) | NO   |     | NULL    |                |
| owner | varchar(150) | NO   |     | NULL    |                |
| birth | date         | NO   |     | NULL    |                |
+-------+--------------+------+-----+---------+----------------+
```

run program with `python ./core.py`
