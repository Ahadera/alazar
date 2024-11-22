import datetime
import streamlit as st

class Library_Master_System:
    def __init__(self, Collection_of_Books, Library_Center_name):
        self.Collection_of_Books = Collection_of_Books
        self.Library_Center_name = Library_Center_name
        self.books_dict = {}
        Books_Id = 0

        try:
            with open(self.Collection_of_Books, 'r') as Books:
                content = Books.readlines()
            for line in content:
                self.books_dict[str(Books_Id)] = {
                    "book_title": line.strip(),
                    "Lender_name": "",
                    "Book_checked_out": "",
                    "Status": "Available"
                }
                Books_Id += 1
        except FileNotFoundError:
            st.error(f"The file '{self.Collection_of_Books}' does not exist.")
        except Exception as e:
            st.error(f"An error occurred while reading the file: {e}")

    def Booking_showing(self):
        st.write("### Collection of Books in the Library")
        for key, value in self.books_dict.items():
            st.write(f"{key}: {value['book_title']} - [{value['Status']}]")

class Checking_books_out(Library_Master_System):
    def Book_check_out(self, Books_Id, your_name):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if Books_Id in self.books_dict.keys():
            if not self.books_dict[Books_Id]["Status"] == "Available":
                st.warning(
                    f"This book is already checked out by {self.books_dict[Books_Id]['Lender_name']} "
                    f"on {self.books_dict[Books_Id]['Book_checked_out']}."
                )
                return

            self.books_dict[Books_Id]["Lender_name"] = your_name
            self.books_dict[Books_Id]["Book_checked_out"] = current_date
            self.books_dict[Books_Id]["Status"] = "Checked Out"
            st.success("Book has been checked out successfully!")
        else:
            st.error("Book information was not found. Please contact a library staff member.")

class adding_books_to_the_collection(Library_Master_System):
    def Adding_Books_to_the_system(self, New_books):
        if len(New_books) > 25:
            st.warning("The book title is too long. Please contact a librarian for further assistance.")
            return
        try:
            with open(self.Collection_of_Books, 'a') as Books:
                Books.writelines(f"{New_books}\n")
            book_id = str(int(max(self.books_dict.keys(), key=int)) + 1)
            self.books_dict[book_id] = {
                "book_title": New_books,
                "Lender_name": "",
                "Book_checked_out": "",
                "Status": "Available"
            }
            st.success(f"The book '{New_books}' has been added to the library collection.")
        except Exception as e:
            st.error(f"Error adding book: {e}")

class returning_book_back_to_the_collection(Library_Master_System):
    def returning_book(self, Book_Id):
        if Book_Id in self.books_dict.keys():
            if self.books_dict[Book_Id]["Status"] == "Available":
                st.warning("This book is already in the library collection.")
                return
            else:
                self.books_dict[Book_Id]["Lender_name"] = ""
                self.books_dict[Book_Id]["Book_checked_out"] = ""
                self.books_dict[Book_Id]["Status"] = "Available"
                st.success("The book has been successfully returned.")
        else:
            st.error("The book ID information was not found in the system.")

# Streamlit App
def main():
    st.title("Library Management System")
    library_file_path = "Library Collection.txt"
    if "Library_system" not in st.session_state:
        st.session_state.Library_system = Library_Master_System(library_file_path, "Python's Library")

    menu = ["Display Books", "Issue Book", "Add Book", "Return Book"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Display Books":
        st.header("Display Books")
        st.session_state.Library_system.Booking_showing()

    elif choice == "Issue Book":
        st.header("Issue a Book")
        book_id = st.text_input("Enter Book ID")
        lender_name = st.text_input("Enter Your Name")
        if st.button("Issue"):
            if book_id and lender_name:
                Checking_books_out(library_file_path, "Python's Library").Book_check_out(book_id, lender_name)

    elif choice == "Add Book":
        st.header("Add a Book")
        new_book = st.text_input("Enter New Book Title")
        if st.button("Add Book"):
            if new_book:
                adding_books_to_the_collection(library_file_path, "Python's Library").Adding_Books_to_the_system(new_book)

    elif choice == "Return Book":
        st.header("Return a Book")
        book_id = st.text_input("Enter Book ID")
        if st.button("Return"):
            if book_id:
                returning_book_back_to_the_collection(library_file_path, "Python's Library").returning_book(book_id)

if __name__ == "__main__":
    main()
