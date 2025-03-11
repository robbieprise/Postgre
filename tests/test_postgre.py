import datetime
from decimal import Decimal
import psycopg2
import pytest
from postgre.postgre import fetch_records

def execute_sql_file(file_path):
    conn = psycopg2.connect(
        dbname="test",
        user="postgres",
        password="postgres",
        host="localhost",
        port=5432
    )

    with open(file_path, 'r', encoding='utf-8') as sql_file:
        sql_data = sql_file.read()
    with conn.cursor() as cur:
        try:
            cur.execute(sql_data)
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(f"エラーが発生しました: {e}")

def test_fetch_records():

    # DBの初期化
    execute_sql_file("sql/start.sql")

    # Call the function
    result = fetch_records()

    assert result == [(1, '名前', '長文テキスト', 100, Decimal('1.25'), True, datetime.datetime(2025, 3, 11, 23, 19, 55, 94000), datetime.datetime(2025, 3, 11, 23, 20, 5, 461000))]

    # DBの後始末
    execute_sql_file("sql/end.sql")
