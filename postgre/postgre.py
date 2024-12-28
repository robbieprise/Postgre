from typing import Any
import psycopg2

def fetch_records():
    """
    指定されたPostgreSQLテーブルからすべてのレコードを取得します。

    提供された接続パラメータを使用してPostgreSQLデータベースに接続し、
    'your_table'からすべてのレコードを選択するクエリを実行し、結果を返します。

    戻り値:
        list: 各タプルがテーブル内の行を表すタプルのリスト。
    """
    # Connect to your postgres DB
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
            cur.execute("SELECT * FROM sample_table")
                
            # Retrieve query results
            records = cur.fetchall()

            return records

