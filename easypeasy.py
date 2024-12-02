import streamlit as st

class LibraryMasterSystem:
    def __init__(self, collection_of_books, library_name):
        self.collection_of_books = collection_of_books
        self.library_name = library_name
        self.books_dict = {}
        self.books_id = 1
        self.load_books()

    def load_books(self):
        try:
            with open(self.collection_of_books, 'r') as file:
                for line in file:
                    book_title = line.strip()
                    if book_title:
                        self.books_dict[str(self.books_id)] = {
                            "book_title": book_title,
                            "lender_name": "",
                            "status": "Available"
                        }
                        self.books_id += 1
        except FileNotFoundError:
            st.warning("Book file not found. Starting with an empty library.")

    def display_books(self):
        st.subheader("Books Available in the Library:")
        # Separate available and checked-out books
        available_books = {book_id: details for book_id, details in self.books_dict.items() if details["status"] == "Available"}
        checked_out_books = {book_id: details for book_id, details in self.books_dict.items() if details["status"] == "Checked Out"}

        if available_books:
            st.write("**Available Books:**")
            for book_id, details in available_books.items():
                st.write(f"ID: {book_id}, Title: {details['book_title']}")
        else:
            st.write("No books available currently.")

        if checked_out_books:
            st.write("**Checked Out Books:**")
            for book_id, details in checked_out_books.items():
                st.write(f"ID: {book_id}, Title: {details['book_title']}, Lender: {details['lender_name']}")
        else:
            st.write("No books are checked out currently.")

class BookManager:
    def __init__(self, library_system):
        self.library_system = library_system

    def check_out_book(self, book_id, lender_name):
        if not book_id.strip() or not lender_name.strip():
            st.warning("Book ID and Lender Name cannot be empty.")
            return

        if book_id not in self.library_system.books_dict:
            st.warning("This book ID does not exist.")
            return

        if self.library_system.books_dict[book_id]["status"] == "Checked Out":
            st.warning("This book is already checked out.")
            return

        # Update book details for checkout
        self.library_system.books_dict[book_id]["lender_name"] = lender_name
        self.library_system.books_dict[book_id]["status"] = "Checked Out"
        st.success("Book has been checked out successfully.")

    def return_book(self, book_id):
        if not book_id.strip():
            st.warning("Book ID cannot be empty.")
            return

        if book_id not in self.library_system.books_dict:
            st.warning("This book ID does not exist.")
            return

        if self.library_system.books_dict[book_id]["status"] == "Available":
            st.warning("This book is already available.")
            return

        # Reset book details for return
        self.library_system.books_dict[book_id]["status"] = "Available"
        self.library_system.books_dict[book_id]["lender_name"] = ""
        st.success("Book has been returned successfully.")

    def add_book(self, book_title):
        # Ensure the book title isn't empty
        if not book_title.strip():
            st.warning("Book title cannot be empty.")
            return

        self.library_system.books_dict[str(self.library_system.books_id)] = {
            "book_title": book_title,
            "lender_name": "",
            "status": "Available"
        }
        self.library_system.books_id += 1
        # Add book to file for persistence
        with open(self.library_system.collection_of_books, 'a') as file:
            file.write(book_title + "\n")
        st.success("Book has been added successfully.")

# Main function for Streamlit application
def main():
    st.title("Library Management System")
    library_system = LibraryMasterSystem("library_books.txt", "My Local Library")
    book_manager = BookManager(library_system)

    # Display available books
    library_system.display_books()

    # Sidebar options for the user
    new_book = st.sidebar.text_input("Enter New Book Title")
    if st.sidebar.button("Add Book"):
        book_manager.add_book(new_book)

    book_id = st.sidebar.text_input("Enter Book ID")
    lender_name = st.sidebar.text_input("Enter Your Name")

    if st.sidebar.button("Issue Book"):
        book_manager.check_out_book(book_id, lender_name)

    if st.sidebar.button("Return Book"):
        book_manager.return_book(book_id)

if __name__ == "__main__":
    main()