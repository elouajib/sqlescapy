from sqlescapy import sqlescape

# assuming this 2 variables are coming from a user input
clean_input = "JhonWick"
dangerous_input = "JhonWick'"

clean_raw_statement = "\"foo_table\".username='%s'" % clean_input
dangerous_raw_statement = "\"foo_table\".username='%s'" % dangerous_input
protected_raw_statement = "\"foo_table\".username='%s'" % sqlescape(dangerous_input)

clean_query = """

SELECT "foo_table".*, "bar_table".*
FROM "foo_table", "bar_table"
WHERE "foo_table".id = "bar_table".id
      AND %s
""" % clean_raw_statement

dangerous_query = """

SELECT "foo_table".*, "bar_table".*
FROM "foo_table", "bar_table"
WHERE "foo_table".id = "bar_table".id
      AND %s
""" % dangerous_raw_statement

protected_query = """

SELECT "foo_table".*, "bar_table".*
FROM "foo_table", "bar_table"
WHERE "foo_table".id = "bar_table".id
      AND %s
""" % protected_raw_statement

# Clean
print(clean_query)
# SQL Syntaxe ERROR and the the attacker can start injecting...
print(dangerous_query)
# Protected query using sqlescapy
print(protected_query)
