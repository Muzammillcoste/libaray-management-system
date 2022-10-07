import sqlite3

# These are all sqlite queries which used in this management system.

Create_Member_Table='''CREATE TABLE IF NOT EXISTS member_info (id INT PRIMARY KEY,
name TEXT, member_id INT, book_id INT, book_name TEXT, issue_date TEXT, recieved_date TEXT);'''

Create_BookShelf_Table='''CREATE TABLE IF NOT EXISTS BookShelf (book_id INT,book_name TEXT,
shelf_no INT) '''

Insert_Member= '''INSERT INTO member_info (name,member_id,book_id,book_name,issue_date,recieved_date)
VALUES (?,?,?,?,?,?);'''

Insert_Book= '''INSERT INTO BookShelf (book_id ,book_name,shelf_no) 
VALUES(?,?,?);'''

Get_All_Member='''SELECT * FROM member_info'''
Get_All_Book='''SELECT * FROM BookShelf'''

Search_Member_BYName='''SELECT * FROM member_info WHERE name=?'''
Search_BOOK_BYBook='''SELECT * FROM BookShelf WHERE Book_name=?'''

def connet():
    return sqlite3.connect('data.db')

def create_member_table(connection):
    with connection:
        connection.execute(Create_Member_Table)
        
def create_bookshelf_table(connection):
    with connection:
        connection.execute(Create_BookShelf_Table)
        
def add_member_info(connetion,name,member_id,book_id,book_name,issue_date,recieved_date):
    with connetion:
        connetion.execute(Insert_Member,(name,member_id,book_id,book_name,issue_date,recieved_date))
        
def add_book(connection,book_id,book_name,shelf_no):
    with connection:
        connection.execute(Insert_Book,(book_id,book_name,shelf_no))
        
def get_all_book(connection):
    with connection:
        return connection.execute(Get_All_Book).fetchall()

def get_all_member(connection):
    with connection:
        return connection.execute(Get_All_Member).fetchall()
    
def search_member_byname(connection,name):
    with connection:
        return connection.execute(Search_Member_BYName,(name,)).fetchall()
    
def search_book_byname(connection,book_name):
    with connection:
        return connection.execute(Search_BOOK_BYBook,(book_name,)).fetchall()
    
