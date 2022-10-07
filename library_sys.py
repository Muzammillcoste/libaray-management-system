import database

SYSTEM_PROMPT='''--LIBRARY MANAGEMENT SYSTEM-- 

Please select one these options:

1) Add member
2) Add book
3) See all book
4) See all member
5) Find a member by name
6) Find a book by name
7) Exit.

Your Selection: '''

def system():
    connection=database.connet()
    database.create_member_table(connection)
    database.create_bookshelf_table(connection)
    
    while(user_input := input(SYSTEM_PROMPT))!='7':
        if user_input=='1':
            name=input('Enter name: ')
            member_id=int(input('Enter member ID: '))
            book_name=input('Enter book name: ')
            book_id=int(input('Enter book ID: '))
            issue_date=input('Enter date of issue: ')
            recieved_date=input('Enter date of received: ')
            database.add_member_info(connection, name, member_id, book_id, book_name, issue_date, recieved_date)
            
        elif user_input=='2':
            book_name=input('Enter book name: ')
            book_id=int(input('Enter book ID: '))
            shelf_no=int(input('Enter shelf no: '))
            database.add_book(connection, book_id, book_name, shelf_no)
            
        elif user_input=='3':
                books=database.get_all_book(connection)
                for book in books:
                    print(f'Book ID:{book[0]}, Book Name:{book[1]}, Shelf No:{book[2]}\n')
        elif user_input=='4':
                members=database.get_all_member(connection)
                for member in members:
                    print(f' Name:{member[1]}, Member ID:{member[2]}, Book ID:{member[3]}, Book Name:{member[4]}, Issue Date:{member[5]}, Received Date:{member[6]}\n')
                    
        elif user_input=='5':
            name=input('Enter name: ')
            members=database.search_member_byname(connection, name)
            for member in members:
                print(f' Name:{member[1]}, Member ID:{member[2]}, Book ID:{member[3]}, Book Name:{member[4]}, Issue Date:{member[5]}, Received Date:{member[6]} ')          
                
        elif user_input=='6':
                book_name=input('Enter book name: ')
                books=database.search_book_byname(connection, book_name)
                for book in books:
                    print(f'Book ID:{book[0]}, Book Name:{book[1]}, Shelf No:{book[2]}')
        else:
            print('Invalid input, try again')   
        
system()