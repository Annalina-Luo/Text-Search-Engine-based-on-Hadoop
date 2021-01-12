import mysql.connector
import pandas as pd
import sys
import os
try:
    # you need to change this part to you own database
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         passwd="1830001064",
                                         db="ws2",
                                         auth_plugin='mysql_native_password',
                                         use_pure=True)

    cursor = connection.cursor()

    name = ""

    i = -1

    for root, dirs, files in os.walk("files"):
        # print("1",os.path.basename(root))
        for filename in files:
            i += 1
            name = filename.replace("'", "\\'").replace('"','\\"')

            print(name)
            filepath = os.path.join(root, filename)
            print(filepath)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            content = content.replace("\\","\\\\").replace("'", "\\'").replace('"','\\"')
            insert_operation = """INSERT INTO articles(name,content)
                        VALUES("{name}","{content}")"""
            print(i,insert_operation.format(name=name, content=" "))
            insert_operation = insert_operation.format(name=name, content=content)
            cursor.execute(insert_operation)



except mysql.connector.Error as msg:
    print(msg)

finally:
    connection.commit()
    if (connection.is_connected()):
        cursor.close()
        connection.close()