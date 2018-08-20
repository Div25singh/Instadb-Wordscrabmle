'''
Created on 11-Aug-2018

@author: anitr
'''
import cx_Oracle
from abc import ABC,abstractmethod

def initialize_db():                                                            #function to connect to db
    db=cx_Oracle.connect('ani/mycycle.com')
    cur=db.cursor()
    try:
        cur.execute("""Create Table user1(
            title varchar2(30) not null,
            author varchar2(20) not null,
            publication varchar2(20) not null
            pub_year number(4) not null,
            id number(5) primary key,
            no_of_books number(3) not null,
            )""")
        db.create_tables([book, member, issue_history])
    except OperationalError:
        # Table already exists. Do nothing
        pass
    
class book():   
    def set_title(self,title):
        self.btitle = title
    def set_author(self,author):
        self.bauthor = author
    def set_publish(self,publication):
        self.bpublication = publication 
    def set_pub_year(self,pub_year):
        self.bpub_year = pub_year
    def set_id(self,b_id):
        self.bid = b_id  
    def set_no_of_books(self,num_of_books):
        self.bnum_of_books = num_of_books
    def get_title(self):
        return self.btitle
    def get_author(self):
        return self.bauthor
    def get_publish(self):
        return self.bpublication
    def get_pub_year(self):
        return self.bpub_year
    def get_id(self):
        return self.bid
    def get_no_of_books(self):
        return self.bnum_of_books

class member():
    def set_user_id(self,user_id):
        self.muser_id = user_id  
    def set_name(self,name):
        self.mname = name
    def set_phone_no(self,phone_no):
        self.mphone_no = phone_no 
    def get_user_id(self):
        return self.muser_id
    def get_name(self):
        return self.mname
    def get_phone_no(self):
        return self.mphone_no                                                         #Table for members

class issue_history(Model):                                                        #Table for issue handling
    user_id = ForeignKeyField
    isbn = ForeignKeyField
    issue_id = CharField()
    issue_date = DateField()
    return_date = DateField()
    current_status = TextField()

def add_book():                                                                    #func to enter a new book
    book_title = raw_input('Enter the book title: ')
    book_author = raw_input('Enter the book author: ')
    book_publication = raw_input('Enter the book publication: ')
    book_pub_year = raw_input('Enter the year of publication of book: ')
    book_isbn = raw_input('Enter the ISBN code of book: ')
    #book_no = number of books having same ISBN
    

def add_book_to_db():                                    #func to actually save books to db
    book_data = """insert into book values(title='book_title',
                        author='book_author',
                        publication='book_publication',
                        pub_year='book_pub_year',
                        isbn='book_isbn',
                        current_status='current_status')"""
    cur.execute(book_data)

def add_member():                                                                #func to add a new member
    user_id = raw_input('Enter the user_id: ')
    member_name = raw_input('Enter the member name: ')
    member_phone_no = raw_input('Enter the phone number of the member: ')


def add_member_to_db(comment, TableName=member):                                #func to actually save a new member to db
    member_data = book(user_id=user_id,
                        name=member_name,
                        phone_no=member_phone_no)
    book_data.save()


def allocate():                                                                    #func to allocate a book
    alloc_book_isbn = raw_input('Enter book isbn to be allocated: ')
    #check alloc_book_id with actual book id in database
    if alloc_book_id in book_isbn:
        alloc_member_id = raw_input('Enter member id receving the book:')
        #checks if correct user_id is entered
        if alloc_member_id in user_id:
            issue_date = raw_input('Enter issueing date:')
            return_date = raw_input('Enter return date:')
            #checks if date is properly entered or not
            if start_date > return_date:
                print ('Issueing date cannot be after return date')
                #go to line 37
            
            else :
                issue_id = issue_date + user_id + return_date 
                issue_data.save()
                issue.append(sr_no)
                current_status = 'issued'
                print 'This is your issue id: {0}'.format(issue_id) 
                print 'Your return date is: {0}'.format(return_date)

        else:
            print ('user_id entered does not exist')
            #go to line line 35
        
    else:
        print ('ISBN entered is not present in the database')
        #go to line 32
    

def save_allocate_to_db(comment, TableName=issue_history):                                #func to save the new allocation data to db
    issue_data = book(user_id=alloc_member_id,
                        isbn=alloc_book_isbn,
                        issue_id=issue_id,
                        issue_date=issue_date,
                        return_date=return_date,
                        num_of_books=book_no)
    issue_data.save()


def de_allocate():                                                                #func to de-allocate a book
    de_alloc_issue_id = raw_input('Enter the issue id provided to you:')
    #check alloc_book_id with actual book id in database
    if de_alloc_issue_id in issue_data:
        if today_date == return_date in issue_data:
            print ('Book received')
            book_no += 1
            current_status = 'returned'

        elif today_date < return_date:
            overdue_days = return_date - today_date
            fine = 5*overdue_days
            print "Your fine is Rs", fine
            current_status = 'returned'

        else:
            book_no+= 1
            print 'Thank you for choosing Python Library'

#def update_de_allocate_to_db():
    #function to add returned status to book


def remove_book():                                                                
    check_isbn = raw_input('Enter the ISBN code of the book you want to remove: ')
    
    for check_isbn in book_isbn(1,10):
        #remove book action
        book = book.get(book_isbn == check_isbn)
        book.delete_instance()

        print 'The book',check_isbn,'has been deleted.'
    



def remove_member():                                                      #func to remove member from db
    rem_member_id = raw_input("Enter member's user_id : ")
    # remove member action
    member = member.get(user_id == rem_member_id)
    member.delete_instance()

    print 'Member',rem_member_id,'has been removed.'
    



print """                                      
         Welcome to Python Library System.
          a To add a book
          b To add a member
          c To allocate a book
         d To return a book
         e To remove a book from the collection
          f To remove a member from the book
     """

user_option = raw_input('Enter your choice now:')
user_option = user_option.lower()





if user_option == 'a':
    add_book()

elif user_option == 'b':
    add_member()
    
elif user_option == 'c':
    allocate()
    
elif user_option == 'd':
    de_allocate()
    
elif user_option == 'e':
    remove_book()
    
elif user_option == 'f':
    remove_member()
else:
    print "Invalid choice"

if __name__ == '__main__':
    initialize_db()
    

