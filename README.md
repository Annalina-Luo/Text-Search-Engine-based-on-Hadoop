# Text-Search-Engine-based-on-Hadoop
This project is a text searching engine based on Hadoop MapReduce. It includes text files collection, MapReduce with inverted index and webpage design using Django.
##### Author: Nicholas ZHONG, Yingfang ZHANG, Zhen LUO
##### Contact: 18928787748@163.com
------------------------------------------------------
### Environment:
##### Linux with Java 1.8.0, Hadoop 3.3.0

##### Windows with Python 3.8
##### Packages requirement: Django1.8, request, BeautifulSoup from bs4, os, mysql.connector, sys, pandas
### IDE: 
PyCharm 2020.3(Professional Version)

-------------------------------------------------------
### Structure
##### 
Text-Search-Engine-based-on-Hadoop<br>
&emsp;&emsp;README.txt<br>
&emsp;&emsp;code<br>
&emsp;&emsp;&emsp;&emsp;crawl_new.py<br>
&emsp;&emsp;&emsp;&emsp;rename.py<br>
&emsp;&emsp;&emsp;&emsp;TDIDF_InvertedIndex.java<br>
&emsp;&emsp;&emsp;&emsp;Database.py<br>
&emsp;&emsp;&emsp;&emsp;blob.py<br>
&emsp;&emsp;&emsp;&emsp;SearchFile.zip<br>
&emsp;&emsp;file<br>
&emsp;&emsp;&emsp;&emsp;big.txt<br>
&emsp;&emsp;&emsp;&emsp;Instruction.docx<br>
&emsp;&emsp;&emsp;&emsp;files.zip<br>
#####
-------------------------------------------------------
### Code
##### crawl_new.py
This python file does web crawling from http://www.gutenberg.org/ebooks and http://www.gutenberg.org/cache/epub/%s/pg. The former URL provides the titles of the books and the latter one provides the content of a specific book. And the text files are in ../file/files folder.
If a text file is crawled successfully, it will print the name of the book in the terminal.

##### rename.py
This python file renames the crawling text files. It replaces the space into underline of the filenames.

##### TDIDF_InvertedIndex.java
This java file does the inverted index job and ranking. Notice that the name of this java file cannot be changed, or it will cause some problems while compilng and creating jar.

##### blob.py
This python file is for another import of database called articles, which contains the article name and the corresponding context.

##### Database.py
This python file is for the split the result file information, and then import these information into Database. The Database is called recode, which contains (word VARCHAR(100), time Interger, article VARCHAR(200). And the database which the code connect is a localhost in local computer, if you want to import to your database, please change the connect method.

##### Searchfile.zip
Include the Django code for websites implementations

-------------------------------------------------------
### file
##### big.txt
This text file is the result of running MapReduce job using Hadoop and inverted index.

##### Instruction.docx
This document instructs you how to conduct MapReduce using Hadoop on Linux operating system.

##### files.zip
This zip file stores all the crawling text files. We manually compress it because it is too big. You can either decompress this zip or run the crawl_new.py. We suggest decompressing because crawling takes a long time.

-------------------------------------------------------
### How to run the code
1. unzip th files.zip and you will get a folder called "files"
2. put the files folder and big.txt into the code folder.
3. In you own database, create a table called 'articles', values("name" VARCHAR(200), "content" LONGTEXT).
4. change the database information in blob.py and Database.py to your own database information and then run these two 
5. unzip the SearchFile.zip, change the database information in views.py.
6. start the Django on SearchFile folder, then you can do many operations in the websites.
7. If you have some questions about big.txt, you can follow the Instruction.docx to do the mapreduce in Linux to get this file.
