class Book:
    def __init__(self,book_name,author,isbn):
         self.book_name=book_name
         self.author=author
         self.isbn=isbn
         self.available=True

    def display_info(self):
         print(f"Book Name: {self.book_name}")
         print(f"Author: {self.author}")
         print(f"ISBN: {self.isbn}")
         print(f"Availability: {'Available' if self.available else 'Borrowed'}")

class Member:
     def __init__(self,member_name,member_id):
          self.member_name=member_name
          self.member_id=member_id
          self.borrowed_books=[]


     def display_borrowed_books(self):
          for book in self.borrowed_books:
               print(f"Books: {book.display_info()}")

class Library:
     def __init__(self):
          self.books=[]
          self.members=[]

     def add_book(self, book):
          self.books.append(book)
     
     def add_member(self,member):
          self.members.append(member)

     def borrow_book(self,member,book):
         
        if member in self.members: 
             if book in self.books:  
               if book.available==True:
                    member.borrowed_books.append(book)
                    book.available=False
               elif book in member.borrowed_books:
                  print("You HAve Already borrowed it")
               else:
                    print("The book is already borrowed")
             else:
                  print("Book not Found")
        else:
             print("Member not found")


     def return_book(self,member,book):
             if member in self.members: 
                  if book in self.books:
                       if book.available:
                            print("Not borrowed Yet")
                       else:
                            if book in member.borrowed_books:
                                 num=member.borrowed_books.index(book)
                                 member.borrowed_books.pop(num)
                                 book.available=True
                            else:
                                 print("Not borrowed by this member")

                  else:
                       print("book not found")
             else:
                  print("Member not registered")
     def search_book(self,book_name):
          for book in self.books:
               if book.book_name == book_name:
                    return book
          return None
     
     def search_member(self,memberid):
          for member in self.members:
               if member.member_id==memberid:
                    return member
          return None
     
     def display_books(self):
        if len(self.books) == 0:
          print("No Book is Available")
        else:
          for book in self.books:
               book.display_info()

     def remove_book(self,book):
          if book in self.books:
               if book.available:
                    num=self.books.index(book)
                    self.books.pop(num)
               else:
                   print("The book is already issued wait for return")
          else:
               print("The book is not registered")

library = Library()

while True:
     
 print("""
      1. Add Book
      2. Register Member
      3. Search Book
      4. Return Book
      5. Borrow Book
      6. Display All Books
      7. Remove Books
      8. Exit
 """)
 
 num=int(input("Enter the number"))

 if num==1:
      book_name=input("Enter the book name")
      author=input("Enter the author name")
      isbn=input("Enter the isbn num")
      new_book=Book(book_name,author,isbn)
      library.add_book(new_book)

 elif num==2:
     member_name=input("Enter the member name")
     member_id=input("member id")
     new_member=Member(member_name,member_id)
     library.add_member(new_member)

 elif num==3:
      book_name=input("Enter the book object you want to search")
      book_obj=library.search_book(book_name)
      print(book_obj)

 elif num==4:
      book_name=input("Enter the book object you want to return")
      book_obj=library.search_book(book_name)
      memberid=input("Enter the member id")
      member_obj=library.search_member(memberid)
      library.return_book(member_obj, book_obj)

  
 elif num==5:
      book_name=input("Enter the book object you want to return")
      book_obj=library.search_book(book_name)
      memberid=input("Enter the member id")
      member_obj=library.search_member(memberid)
      library.borrow_book(member_obj,book_obj)

 elif num == 6:
      library.display_books()

 elif num == 7:
      book_name=input("Enter the book object you want to return")
      book_obj=library.search_book(book_name)
      library.remove_book(book_obj)
 elif num == 8:
      break
