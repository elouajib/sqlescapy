Python module to escape SQL special characters and quotes in strings

install:
`pip install sqlescapy`

Assuming `dangerous_input` is a variable coming from a user input, a bad actor can exploit it to start injecting your database.
```python
from sqlescapy import sqlescape

dangerous_input = "JhonWick'"

protected_raw_statement = "\"foo_table\".username='%s'" % sqlescape(dangerous_input)

protected_query = """

SELECT "foo_table".*, "bar_table".*
FROM "foo_table", "bar_table"
WHERE "foo_table".id = "bar_table".id
      AND %s
""" % protected_raw_statement

```
