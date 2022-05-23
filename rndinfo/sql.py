import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE users
    (first_name,
    last_name,
    gender,
    hobbies,
    street,
    area,
    landmark,
    province,
    city,
    zip
    );''')


def insert(data: list):
    """
    Fill user table
    :param data: list user data
    """
    if len(data) < 10:
        for i in range(10-len(data)):
            data.append("")
    # Insert a row of data
    data_string = "'"+"','".join(data)+"'"
    cur.execute(f"INSERT INTO users VALUES ({data_string})")
    # Save (commit) the changes
    con.commit()


def get_equal(field, value):
    return cur.execute(f'SELECT * FROM users WHERE {field} LIKE "%{value}%";').fetchall()


def get_not(field, value):
    return cur.execute(f'SELECT {field} FROM users WHERE {field} <> "{value}";').fetchall()


def get_any():
    return cur.execute(f'SELECT * FROM users;').fetchall()


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
# con.close()
