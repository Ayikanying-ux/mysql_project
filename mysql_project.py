# coonect python with mysql

import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "execute",
    database = "library"
    )
cursor = db.cursor()

#ask user to add books
def add_books():
    add_books = input("Do you want to add books to database: ")
    print("\n")

    print("If you dont want to add books type: 0")
    print("\n")

    number = int(input("Enter number of books you want to add: "))

    if add_books == "YES" and number>=1:
        for i in range(number):
            book_name = input("Enter name of the book: ")
            author = input("Enter author of the book: ")
            query = "INSERT INTO books (name, author) VALUES (%s, %s)"
            values = (book_name, author) 
            cursor.execute(query, values)
            db.commit()
    elif add_books == "NO" and number == 0:
        print("No book will be added")

    elif add_books == "YES" and number == 0:
        print("Number has to be equal or greater than one")
        print("\n")
    elif add_books == "NO" and number ==1:
        print("Number has to be zero if you don't want to add any books")
    print("\n")
add_books()

def display_books():  
    query = "SELECT * FROM books"

    cursor.execute(query)

    records = cursor.fetchall()

    print("Below are the books in you library")
    for record in records:
        print(record)
        print("\n")
display_books()

def sell_books():
    sale = input("Do you want to sell any books: ")
    if sale == "YES":
        book_to_sale = input("Enter the name of the book you which to sell: ")
        query = "DELETE FROM books WHERE name=%s"
        value = (book_to_sale,)
        cursor.execute(query, value)
        db.commit()
        print("Book has been sold")
    elif sale == "NO":
        print("Thank you for using our service")
sell_books()

display_books()