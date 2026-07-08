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
         print(f"Availability: {"Available" if self.available else "Borrowed"}")

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
     
     def display_books(self):
        if len(self.books) == 0:
          print("No Book is Available")
        else:
          for book in self.books:
               print(book.display_info())

     def remove_book(self,book):
          if book in self.books:
               if book.available:
                    num=self.books.index(book)
                    self.books.pop(num)
               else:
                   print("The book is already issued wait for return")
          else:
               print("The book is not registered")



book1=Book("Clean Code", "Roberto C. Martin", "12345")
member1=Member("Aashir","bs-1")
library = Library()

library.add_book(book1)
library.add_member(member1)