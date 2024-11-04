"""
Unit test for : verifying ids of different employees
"""

from mydb import MyDB

import pytest

@pytest.fixture()
def cur():
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("Closing the Database...")

def test_john_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_tom_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789