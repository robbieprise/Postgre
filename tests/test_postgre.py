import datetime
from decimal import Decimal
import psycopg2
import pytest
from postgre.postgre import fetch_records

@pytest.fixture(scope="function")
def create_data():
    conn = psycopg2.connect(
        dbname="test",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )

    with conn:
        with conn.cursor() as cur:
            # SQLクエリの実行
            try:
                cur.execute("TRUNCATE TABLE sample_table;")
                cur.execute(
                    "INSERT INTO sample_table " +
                    "(name,description,quantity,price,is_active,created_at,updated_at) " + 
                    "VALUES " +
                    "('名前','長文テキスト',100,1.25,True,TIMESTAMP '2024-12-28 23:19:55.094',TIMESTAMP '2024-12-28 23:20:05.461');")
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(f"エラーが発生しました: {e}")

    yield

    with conn:
        with conn.cursor() as cur:
            # SQLクエリの実行
            try:
                cur.execute("TRUNCATE TABLE sample_table;")
                conn.commit()
            except Exception as e:
                conn.rollback()
                print(f"エラーが発生しました: {e}")



def test_fetch_records():

    # Call the function
    result = fetch_records()

    assert result == [(1, '名前', '長文テキスト', 100, Decimal('1.25'), True, datetime.datetime(2024, 12, 28, 23, 19, 55, 94000), datetime.datetime(2024, 12, 28, 23, 20, 5, 461000))]

