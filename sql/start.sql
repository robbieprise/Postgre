TRUNCATE TABLE sample_table;

INSERT INTO sample_table
    (id,name,description,quantity,price,is_active,created_at,updated_at)
VALUES
    (1,'名前','長文テキスト',100,1.25,True,TIMESTAMP '2024-12-28 23:19:55.094',TIMESTAMP '2024-12-28 23:20:05.461');

