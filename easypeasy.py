import datetime
import streamlit as st

# Main Library Class
class LibraryMasterSystem:
    def __init__(self, library_center_name):
        self.library_center_name = library_center_name
        self.books_dict =  [
    {"ID": "000", "Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Minor Damage Fine": 20, "Severe Damage Fine": 80},
    {"ID": "001", "Title": "1984", "Author": "George Orwell", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "002", "Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "003", "Title": "Pride and Prejudice", "Author": "Jane Austen", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "004", "Title": "Moby Dick", "Author": "Herman Melville", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "005", "Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Minor Damage Fine": 15, "Severe Damage Fine": 55},
    {"ID": "006", "Title": "The Hobbit", "Author": "J.R.R. Tolkien", "Minor Damage Fine": 10, "Severe Damage Fine": 35},
    {"ID": "007", "Title": "War and Peace", "Author": "Leo Tolstoy", "Minor Damage Fine": 12, "Severe Damage Fine": 40},
    {"ID": "008", "Title": "The Brothers Karamazov", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 20, "Severe Damage Fine": 60},
    {"ID": "009", "Title": "The Odyssey", "Author": "Homer", "Minor Damage Fine": 18, "Severe Damage Fine": 55},
    {"ID": "010", "Title": "Jane Eyre", "Author": "Charlotte Brontë", "Minor Damage Fine": 12, "Severe Damage Fine": 50},
    {"ID": "011", "Title": "Crime and Punishment", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "012", "Title": "Brave New World", "Author": "Aldous Huxley", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "013", "Title": "Wuthering Heights", "Author": "Emily Brontë", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "014", "Title": "The Divine Comedy", "Author": "Dante Alighieri", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "015", "Title": "Don Quixote", "Author": "Miguel de Cervantes", "Minor Damage Fine": 20, "Severe Damage Fine": 60},
    {"ID": "016", "Title": "Frankenstein", "Author": "Mary Shelley", "Minor Damage Fine": 18, "Severe Damage Fine": 55},
    {"ID": "017", "Title": "The Iliad", "Author": "Homer", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "018", "Title": "Les Misérables", "Author": "Victor Hugo", "Minor Damage Fine": 12, "Severe Damage Fine": 50},
    {"ID": "019", "Title": "Dracula", "Author": "Bram Stoker", "Minor Damage Fine": 20, "Severe Damage Fine": 60},
    {"ID": "020", "Title": "The Count of Monte Cristo", "Author": "Alexandre Dumas", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "021", "Title": "A Tale of Two Cities", "Author": "Charles Dickens", "Minor Damage Fine": 18, "Severe Damage Fine": 55},
    {"ID": "022", "Title": "Anna Karenina", "Author": "Leo Tolstoy", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "023", "Title": "The Scarlet Letter", "Author": "Nathaniel Hawthorne", "Minor Damage Fine": 18, "Severe Damage Fine": 55},
    {"ID": "024", "Title": "Middlemarch", "Author": "George Eliot", "Minor Damage Fine": 10, "Severe Damage Fine": 35},
    {"ID": "025", "Title": "One Hundred Years of Solitude", "Author": "Gabriel García Márquez", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "026", "Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Minor Damage Fine": 20, "Severe Damage Fine": 60},
    {"ID": "027", "Title": "The Adventures of Huckleberry Finn", "Author": "Mark Twain", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "028", "Title": "The Road", "Author": "Cormac McCarthy", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "029", "Title": "Beloved", "Author": "Toni Morrison", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "030", "Title": "The Handmaid's Tale", "Author": "Margaret Atwood", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "031", "Title": "The Great Alone", "Author": "Kristin Hannah", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "032", "Title": "The Hunger Games", "Author": "Suzanne Collins", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "033", "Title": "The Kite Runner", "Author": "Khaled Hosseini", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "034", "Title": "The Alchemist", "Author": "Paulo Coelho", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "035", "Title": "The Shining", "Author": "Stephen King", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "036", "Title": "The Night Circus", "Author": "Erin Morgenstern", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "037", "Title": "The Shadow of the Wind", "Author": "Carlos Ruiz Zafón", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "038", "Title": "Dune", "Author": "Frank Herbert", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "039", "Title": "The Martian", "Author": "Andy Weir", "Minor Damage Fine": 18, "Severe Damage Fine": 55},
    {"ID": "040", "Title": "The Goldfinch", "Author": "Donna Tartt", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "041", "Title": "The Girl on the Train", "Author": "Paula Hawkins", "Minor Damage Fine": 20, "Severe Damage Fine": 60},
    {"ID": "042", "Title": "Big Little Lies", "Author": "Liane Moriarty", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "043", "Title": "Gone Girl", "Author": "Gillian Flynn", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "044", "Title": "The Outsiders", "Author": "S.E. Hinton", "Minor Damage Fine": 12, "Severe Damage Fine": 50},
    {"ID": "045", "Title": "Catch-22", "Author": "Joseph Heller", "Minor Damage Fine": 8, "Severe Damage Fine": 30},
    {"ID": "046", "Title": "The Secret Garden", "Author": "Frances Hodgson Burnett", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "047", "Title": "Little Women", "Author": "Louisa May Alcott", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "048", "Title": "Harry Potter and the Sorcerer's Stone", "Author": "J.K. Rowling", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "049", "Title": "Percy Jackson & the Olympians: The Lightning Thief", "Author": "Rick Riordan", "Minor Damage Fine": 10, "Severe Damage Fine": 35},
    {"ID": "050", "Title": "A Game of Thrones", "Author": "George R.R. Martin", "Minor Damage Fine": 20, "Severe Damage Fine": 60},
    {"ID": "051", "Title": "The Maze Runner", "Author": "James Dashner", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "052", "Title": "Divergent", "Author": "Veronica Roth", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "053", "Title": "The Fault in Our Stars", "Author": "John Green", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "054", "Title": "Looking for Alaska", "Author": "John Green", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "055", "Title": "Paper Towns", "Author": "John Green", "Minor Damage Fine": 15, "Severe Damage Fine": 50},
    {"ID": "056", "Title": "The Book Thief", "Author": "Markus Zusak", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "057", "Title": "The Perks of Being a Wallflower", "Author": "Stephen Chbosky", "Minor Damage Fine": 10, "Severe Damage Fine": 40},
    {"ID": "058", "Title": "Eleanor & Park", "Author": "Rainbow Rowell", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
    {"ID": "059", "Title": "All the Light We Cannot See", "Author": "Anthony Doerr", "Minor Damage Fine": 12, "Severe Damage Fine": 45},
]


    def display_books(self):
        st.write("### Collection of Books in the Library ###")
        for book_id, book_info in self.books_dict.items():
            st.write(
                f"ID: {book_id} | Title: {book_info['book_title']} | Status: {book_info['status']} | "
                f"Damage Fine: ${book_info['damage_fine']['minor']} (Minor), "
                f"${book_info['damage_fine']['severe']} (Severe)"
            )

# CheckOut Books Class
class CheckOutBooks(LibraryMasterSystem):
    def book_check_out(self, book_id, your_name):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if book_id not in self.books_dict:
            st.error("Invalid Book ID. Please enter a valid Book ID from the list.")
            return

        if self.books_dict[book_id]["status"] != "Available":
            st.warning(
                f"This book is already checked out by {self.books_dict[book_id].get('lender_name', 'Unknown')} "
                f"on {self.books_dict[book_id].get('book_checked_out', 'Unknown date')}."
            )
            return

        self.books_dict[book_id]["lender_name"] = your_name
        self.books_dict[book_id]["book_checked_out"] = current_date
        self.books_dict[book_id]["status"] = "Checked Out"
        st.success("Book has been checked out successfully!")

# Add Books Class
class AddBooksToCollection(LibraryMasterSystem):
    def add_books_to_system(self, new_book_title, minor_damage_fine, severe_damage_fine):
        new_book_id = str(len(self.books_dict)).zfill(3)
        self.books_dict[new_book_id] = {
            "book_title": new_book_title,
            "damage_fine": {"minor": minor_damage_fine, "severe": severe_damage_fine},
            "status": "Available"
        }
        st.success(f"The book '{new_book_title}' has been added to the library collection.")

# Return Books Class
class ReturnBookToCollection(LibraryMasterSystem):
    def return_book(self, book_id):
        if book_id not in self.books_dict:
            st.error("The book ID information was not found in the system.")
            return

        if self.books_dict[book_id]["status"] == "Checked Out":
            self.books_dict[book_id]["lender_name"] = ""
            self.books_dict[book_id]["book_checked_out"] = ""
            self.books_dict[book_id]["status"] = "Available"
            st.success("The book has been successfully returned.")
        else:
            st.warning("This book is already in the library collection and not checked out.")

# Streamlit App
def main():
    st.title("Library Management System")

    if "library_system" not in st.session_state:
        st.session_state.library_system = LibraryMasterSystem("Python's Library")

    menu = ["Display Books", "Issue Book", "Add Book", "Return Book"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Display Books":
        st.header("Display Books")
        st.session_state.library_system.display_books()

    elif choice == "Issue Book":
        st.header("Issue a Book")
        st.session_state.library_system.display_books()
        book_selection = st.selectbox(
            "Select a Book",
            options=[
                (book_id, book_info["book_title"])
                for book_id, book_info in st.session_state.library_system.books_dict.items()
                if book_info["status"] == "Available"
            ],
            format_func=lambda x: x[1] if x else "Select a book",
        )
        your_name = st.text_input("Enter Your Name")
        if st.button("Check Out Book"):
            if book_selection and your_name:
                check_out_system = CheckOutBooks("Python's Library")
                check_out_system.book_check_out(book_selection[0], your_name)
            else:
                st.warning("Please select a book and enter your name.")

    elif choice == "Add Book":
        st.header("Add a New Book")
        new_book_title = st.text_input("Enter the Book Title")
        minor_damage_fine = st.number_input("Enter the Fine for Minor Damage", min_value=1, step=1)
        severe_damage_fine = st.number_input("Enter the Fine for Severe Damage", min_value=1, step=1)
        if st.button("Add Book"):
            if new_book_title and minor_damage_fine and severe_damage_fine:
                add_books_system = AddBooksToCollection("Python's Library")
                add_books_system.add_books_to_system(new_book_title, minor_damage_fine, severe_damage_fine)
            else:
                st.warning("Please fill in all fields to add a new book.")

    elif choice == "Return Book":
        st.header("Return a Book")
        st.session_state.library_system.display_books()
        book_selection = st.selectbox(
            "Select a Book to Return",
            options=[
                (book_id, book_info["book_title"])
                for book_id, book_info in st.session_state.library_system.books_dict.items()
                if book_info["status"] == "Checked Out"
            ],
            format_func=lambda x: x[1] if x else "Select a book",
        )
        if st.button("Return Book"):
            if book_selection:
                return_books_system = ReturnBookToCollection("Python's Library")
                return_books_system.return_book(book_selection[0])
            else:
                st.warning("Please select a book to return.")

if __name__ == "__main__":
    main()
