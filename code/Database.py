import mysql.connector
import pandas as pd

word = []
time = []
article = []

with open(r"big.txt", "rb") as f:

    print('-------------')
    data = f.readlines()
    print('-------------')
    for line in data:
        print(len(data))
        print(line)
        a = line.strip(r'\n'.encode())
        print("a is ",a)
        b = a.split()
        print("b is ",b)
        article_number = len(b) - 1
        for i in range(0, article_number):
            word.append(str(b[0]).split('\'')[1].replace("'", "\\'").replace('"',''))
            time1 = b[i+1].split(':'.encode())[0]
            article1 = b[i+1].split(':'.encode())[1]
            time.append(str(time1).split('\'')[1].replace("'", "\\'").replace('"',''))
            article.append(str(article1).split('\'')[1].replace("'", "\\'").replace('"',''))
        print('------------------------')

try:
    # you need to change this part to you own database
    connection = mysql.connector.connect(host="localhost",
                                         user="root",
                                         passwd="1830001064",
                                         db="ws2",
                                         auth_plugin='mysql_native_password',
                                         use_pure=True)

    cursor = connection.cursor()

    cre_operation1 = """CREATE TABLE record (word VARCHAR(100), time Interger, article VARCHAR(200));"""
    cursor.execute(cre_operation1)
    for i in range(0, len(word)):
        insert_operation = """INSERT INTO record(word,time,article)
                        VALUES("{word}","{time}","{article}")"""
        insert_operation = insert_operation.format(word=word[i], time=time[i], article=article[i])
        print(i,insert_operation)
        cursor.execute(insert_operation)



except mysql.connector.Error as msg:
    print(msg)
except:
    print("Exception")
finally:
    connection.commit()
    if (connection.is_connected()):
        cursor.close()
        connection.close()
