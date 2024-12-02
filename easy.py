import datetime
import os
import streamlit as st

class LibraryMasterSystem:
    def __init__(self, collection_of_books, library_center_name):
        self.collection_of_books = collection_of_books
        self.library_center_name = library_center_name
        self.books_dict = {}
        self.books_id = 0
        
        # Ensure file exists or create a new one
        if not os.path.exists(self.collection_of_books):
            with open(self.collection_of_books, 'w') as _:
                pass

        self.load_books()

    def load_books(self):
        try:
            with open(self.collection_of_books, 'r') as books_file:
                for line in books_file:
                    self.books_dict[str(self.books_id)] = {
                        "book_title": line.strip(),
                        "lender_name": "",
                        "book_checked_out": "",
                        "status": "Available"
                    }
                    self.books_id += 1
        except Exception as e:
            st.error(f"An error occurred while reading the file: {e}")

    def display_books(self):
        st.write("### Collection of Books in the Library")
        for key, value in self.books_dict.items():
            st.write(f"{key}: {value['book_title']} - [{value['status']}]")

class CheckOutBooks(LibraryMasterSystem):
    def book_check_out(self, book_id, your_name):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if book_id not in self.books_dict:
            st.error("Invalid Book ID. Please enter a valid Book ID from the list.")
            return

        if self.books_dict[book_id]["status"] != "Available":
            st.warning(
                f"This book is already checked out by {self.books_dict[book_id]['lender_name']} "
                f"on {self.books_dict[book_id]['book_checked_out']}."
            )
            return

        self.books_dict[book_id]["lender_name"] = your_name
        self.books_dict[book_id]["book_checked_out"] = current_date
        self.books_dict[book_id]["status"] = "Checked Out"
        st.success("Book has been checked out successfully!")

class AddBooksToCollection(LibraryMasterSystem):
    def add_books_to_system(self, new_book):
        if len(new_book) > 25:
            st.warning("The book title is too long. Please contact a librarian for further assistance.")
            return
        try:
            with open(self.collection_of_books, 'a') as books_file:
                books_file.write(f"{new_book}\n")
            book_id = str(len(self.books_dict))
            self.books_dict[book_id] = {
                "book_title": new_book,
                "lender_name": "",
                "book_checked_out": "",
                "status": "Available"
            }
            st.success(f"The book '{new_book}' has been added to the library collection.")
        except Exception as e:
            st.error(f"Error adding book: {e}")

class ReturnBookToCollection(LibraryMasterSystem):
    def return_book(self, book_id):
        if book_id in self.books_dict:
            if self.books_dict[book_id]["status"] == "Available":
                st.warning("This book is already in the library collection.")
                return
            else:
                self.books_dict[book_id]["lender_name"] = ""
                self.books_dict[book_id]["book_checked_out"] = ""
                self.books_dict[book_id]["status"] = "Available"
                st.success("The book has been successfully returned.")
        else:
            st.error("The book ID information was not found in the system.")

# Streamlit App
def main():
    st.title("Library Management System")
    library_file_path = "Library_Collection.txt"

    if "library_system" not in st.session_state:
        st.session_state.library_system = LibraryMasterSystem(library_file_path, "Python's Library")

    menu = ["Display Books", "Issue Book", "Add Book", "Return Book"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Display Books":
        st.header("Display Books")
        st.session_state.library_system.display_books()

    elif choice == "Issue Book":
        st.header("Issue a Book")
        book_id = st.text_input("Enter Book ID")
        your_name = st.text_input("Enter Your Name")
        if st.button("Check Out Book"):
            if book_id and your_name:
                check_out_system = CheckOutBooks(library_file_path, "Python's Library")
                check_out_system.book_check_out(book_id, your_name)
            else:
                st.warning("Please enter both Book ID and your name.")

    elif choice == "Add Book":
        st.header("Add a New Book")
        new_book_title = st.text_input("Enter the Book Title")
        if st.button("Add Book"):
            add_book_system = AddBooksToCollection(library_file_path, "Python's Library")
            add_book_system.add_books_to_system(new_book_title)

    elif choice == "Return Book":
        st.header("Return a Book")
        book_id_to_return = st.text_input("Enter Book ID to Return")
        if st.button("Return Book"):
            return_book_system = ReturnBookToCollection(library_file_path, "Python's Library")
            return_book_system.return_book(book_id_to_return)

if __name__ == "__main__":
    main()

