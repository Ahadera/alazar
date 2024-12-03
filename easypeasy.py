import streamlit as st
import datetime
import logging

# Set up logging
logging.basicConfig(filename='library_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Book class
class Book:
    def __init__(self, title, author, isbn, damage_fee=20):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.damaged = False
        self.damage_fee = damage_fee
        self.waitlist = []

    def __repr__(self):
        status = 'Available' if self.is_available else 'Checked Out'
        damage_status = 'Damaged' if self.damaged else 'Good Condition'
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}, {damage_status}"

    def add_to_waitlist(self, member):
        self.waitlist.append(member)
        logging.info(f"{member.name} added to waitlist for '{self.title}'.")

    def notify_waitlist(self):
        if self.waitlist:
            member = self.waitlist.pop(0)
            logging.info(f"Notified {member.name} about '{self.title}' availability.")

# Member class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = {}
        self.fines = 0

    def borrow_book(self, book, due_date):
        if book.is_available:
            book.is_available = False
            self.borrowed_books[book] = due_date
            logging.info(f"{self.name} borrowed '{book.title}'. Due date: {due_date}")
        else:
            book.add_to_waitlist(self)

    def return_book(self, book, damaged=False):
        if book not in self.borrowed_books:
            return False
        book.is_available = True
        del self.borrowed_books[book]
        if damaged:
            book.damaged = True
            self.fines += book.damage_fee
            logging.info(f"{self.name} returned '{book.title}' damaged. Fine: ${book.damage_fee}")
        book.notify_waitlist()
        return True

    def calculate_fines(self):
        today = datetime.date.today()
        for book, due_date in self.borrowed_books.items():
            if today > due_date:
                overdue_days = (today - due_date).days
                fine = overdue_days * 1.25
                self.fines += fine

        return self.fines

# Library class
class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, title, author, isbn, damage_fee=20):
        if isbn in self.books:
            return False
        new_book = Book(title, author, isbn, damage_fee)
        self.books[isbn] = new_book
        logging.info(f"Added book: {new_book}")
        return True

    def register_member(self, name, member_id):
        if member_id in self.members:
            return False
        new_member = Member(name, member_id)
        self.members[member_id] = new_member
        logging.info(f"Registered member: {new_member.name} (ID: {new_member.member_id})")
        return True

    def search_book(self, search_term):
        return [book for book in self.books.values() if search_term.lower() in book.title.lower() or search_term.lower() in book.author.lower()]

    def show_member_info(self, member_id):
        return self.members.get(member_id, None)

# Streamlit Interface
library = Library()

st.title("Library Management System")

# Tabs for different actions
tabs = st.tabs(["Add Book", "Register Member", "Search & Borrow", "Member Info"])

# Add Book tab
with tabs[0]:
    st.subheader("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    isbn = st.text_input("ISBN")
    damage_fee = st.number_input("Damage Fee", min_value=0, value=20)

    if st.button("Add Book"):
        if library.add_book(title, author, isbn, damage_fee):
            st.success("Book added successfully!")
        else:
            st.error("Book already exists.")

# Register Member tab
with tabs[1]:
    st.subheader("Register a New Member")
    name = st.text_input("Member Name")
    member_id = st.text_input("Member ID")

    if st.button("Register Member"):
        if library.register_member(name, member_id):
            st.success("Member registered successfully!")
        else:
            st.error("Member ID already exists.")

# Search & Borrow tab
with tabs[2]:
    st.subheader("Search and Borrow Books")
    search_term = st.text_input("Search by Title or Author")
    if st.button("Search"):
        results = library.search_book(search_term)
        if results:
            st.write("Search Results:")
            for book in results:
                st.write(f"- {book}")
        else:
            st.error("No books found.")

    isbn_to_borrow = st.text_input("Enter ISBN to Borrow")
    member_id = st.text_input("Enter Your Member ID")
    if st.button("Borrow Book"):
        book = library.books.get(isbn_to_borrow, None)
        member = library.members.get(member_id, None)
        if book and member:
            due_date = datetime.date.today() + datetime.timedelta(days=14)
            member.borrow_book(book, due_date)
            st.success(f"Book borrowed successfully! Due date: {due_date}")
        else:
            st.error("Invalid ISBN or Member ID.")

# Member Info tab
with tabs[3]:
    st.subheader("View Member Info")
    member_id = st.text_input("Enter Member ID")
    if st.button("View Info"):
        member = library.show_member_info(member_id)
        if member:
            st.write(f"**Name**: {member.name}")
            st.write("**Borrowed Books**:")
            for book, due_date in member.borrowed_books.items():
                st.write(f"- '{book.title}' (Due: {due_date})")
            st.write(f"**Fines**: ${member.calculate_fines():.2f}")
        else:
            st.error("Member not found.")
