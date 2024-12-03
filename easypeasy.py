import streamlit as st

class LibrarySystem:
    def __init__(self):
           self.members = {}
           self.checked_out_books = {}
           self.books_dict = {
    "001": {"Title": "1984", "Author": "George Orwell", "Minor Damage Fine": 10, "Severe Damage Fine": 35, "Status": "Available", "Due Date": None},
    "002": {"Title": "Moby-Dick", "Author": "Herman Melville", "Minor Damage Fine": 15, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "003": {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "004": {"Title": "Pride and Prejudice", "Author": "Jane Austen", "Minor Damage Fine": 10, "Severe Damage Fine": 40, "Status": "Available", "Due Date": None},
    "005": {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "006": {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "007": {"Title": "Jane Eyre", "Author": "Charlotte Brontë", "Minor Damage Fine": 11, "Severe Damage Fine": 42, "Status": "Available", "Due Date": None},
    "008": {"Title": "The Lord of the Rings", "Author": "J.R.R. Tolkien", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "009": {"Title": "The Hobbit", "Author": "J.R.R. Tolkien", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "010": {"Title": "Crime and Punishment", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "011": {"Title": "War and Peace", "Author": "Leo Tolstoy", "Minor Damage Fine": 25, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "012": {"Title": "Anna Karenina", "Author": "Leo Tolstoy", "Minor Damage Fine": 22, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "013": {"Title": "Don Quixote", "Author": "Miguel de Cervantes", "Minor Damage Fine": 18, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "014": {"Title": "The Brothers Karamazov", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 21, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "015": {"Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "016": {"Title": "The Odyssey", "Author": "Homer", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "017": {"Title": "The Iliad", "Author": "Homer", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "018": {"Title": "The Divine Comedy", "Author": "Dante Alighieri", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "019": {"Title": "Frankenstein", "Author": "Mary Shelley", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "020": {"Title": "Dracula", "Author": "Bram Stoker", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "021": {"Title": "The Adventures of Huckleberry Finn", "Author": "Mark Twain", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "022": {"Title": "Catch-22", "Author": "Joseph Heller", "Minor Damage Fine": 16, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "023": {"Title": "Slaughterhouse-Five", "Author": "Kurt Vonnegut", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "024": {"Title": "The Road", "Author": "Cormac McCarthy", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "025": {"Title": "Beloved", "Author": "Toni Morrison", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "026": {"Title": "The Color Purple", "Author": "Alice Walker", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "027": {"Title": "Of Mice and Men", "Author": "John Steinbeck", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "028": {"Title": "East of Eden", "Author": "John Steinbeck", "Minor Damage Fine": 16, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "029": {"Title": "The Grapes of Wrath", "Author": "John Steinbeck", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "030": {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "031": {"Title": "The Shining", "Author": "Stephen King", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "032": {"Title": "Carrie", "Author": "Stephen King", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "033": {"Title": "It", "Author": "Stephen King", "Minor Damage Fine": 20, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "034": {"Title": "The Stand", "Author": "Stephen King", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "035": {"Title": "The Dark Tower", "Author": "Stephen King", "Minor Damage Fine": 22, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "036": {"Title": "The Girl with the Dragon Tattoo", "Author": "Stieg Larsson", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "037": {"Title": "The Hunger Games", "Author": "Suzanne Collins", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "038": {"Title": "Divergent", "Author": "Veronica Roth", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "039": {"Title": "The Maze Runner", "Author": "James Dashner", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "040": {"Title": "The Handmaid's Tale", "Author": "Margaret Atwood", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "041": {"Title": "The Left Hand of Darkness", "Author": "Ursula K. Le Guin", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "042": {"Title": "Fahrenheit 451", "Author": "Ray Bradbury", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "043": {"Title": "Brave New World", "Author": "Aldous Huxley", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "044": {"Title": "The Giver", "Author": "Lois Lowry", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "045": {"Title": "The Road", "Author": "Cormac McCarthy", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "046": {"Title": "A Clockwork Orange", "Author": "Anthony Burgess", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "047": {"Title": "The Road", "Author": "Cormac McCarthy", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "048": {"Title": "Ready Player One", "Author": "Ernest Cline", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "049": {"Title": "Neuromancer", "Author": "William Gibson", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "050": {"Title": "The Underground Railroad", "Author": "Colson Whitehead", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "051": {"Title": "The Night Circus", "Author": "Erin Morgenstern", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "052": {"Title": "The Goldfinch", "Author": "Donna Tartt", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "053": {"Title": "The Help", "Author": "Kathryn Stockett", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "054": {"Title": "Little Women", "Author": "Louisa May Alcott", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "055": {"Title": "The Secret Garden", "Author": "Frances Hodgson Burnett", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "056": {"Title": "The Fault in Our Stars", "Author": "John Green", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "057": {"Title": "Looking for Alaska", "Author": "John Green", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "058": {"Title": "Perks of Being a Wallflower", "Author": "Stephen Chbosky", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "059": {"Title": "Eleanor Oliphant Is Completely Fine", "Author": "Gail Honeyman", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "060": {"Title": "The Night Manager", "Author": "John le Carré", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "061": {"Title": "Atonement", "Author": "Ian McEwan", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "062": {"Title": "The English Patient", "Author": "Michael Ondaatje", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "063": {"Title": "The Kite Runner", "Author": "Khaled Hosseini", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "064": {"Title": "The Lovely Bones", "Author": "Alice Sebold", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "065": {"Title": "Room", "Author": "Emma Donoghue", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "066": {"Title": "Life After Life", "Author": "Kate Atkinson", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "067": {"Title": "The Time Traveler's Wife", "Author": "Audrey Niffenegger", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "068": {"Title": "The Girl on the Train", "Author": "Paula Hawkins", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "069": {"Title": "The Woman in White", "Author": "Wilkie Collins", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "070": {"Title": "Rebecca", "Author": "Daphne du Maurier", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "071": {"Title": "The Turn of the Screw", "Author": "Henry James", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "072": {"Title": "The House on Mango Street", "Author": "Sandra Cisneros", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "073": {"Title": "The Bell Jar", "Author": "Sylvia Plath", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "074": {"Title": "Never Let Me Go", "Author": "Kazuo Ishiguro", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "075": {"Title": "A Little Life", "Author": "Hanya Yanagihara", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
}
    

    def add_member(self, member_id, name):
        if member_id not in self.members:
            self.members[member_id] = {"Name": name, "Checked Out": []}
            st.success(f"Member {name} added successfully.")
        else:
            st.warning(f"Member {name} already exists.")

    def display_books(self):
        available_books = {book_id: details["Title"] for book_id, details in self.books_dict.items() if details["Status"] == "Available"}
        if available_books:
            st.write("Available Books:")
            for book_id, title in available_books.items():
                st.write(f"{book_id}: {title}")
        else:
            st.write("No books available currently.")

    def checkout_book(self, member_id, book_id):
        if member_id not in self.members:
            st.warning("Member not found.")
            return
        if book_id not in self.books_dict or self.books_dict[book_id]["Status"] != "Available":
            st.warning("Book is not available for checkout.")
            return
        self.books_dict[book_id]["Status"] = "Checked Out"
        self.members[member_id]["Checked Out"].append(book_id)
        self.checked_out_books[book_id] = member_id
        st.success(f"Book {self.books_dict[book_id]['Title']} checked out successfully.")

    def return_book(self, member_id, book_id):
        if member_id not in self.members or book_id not in self.members[member_id]["Checked Out"]:
            st.warning("Invalid return attempt.")
            return
        self.members[member_id]["Checked Out"].remove(book_id)
        self.books_dict[book_id]["Status"] = "Available"
        fine = self.calculate_fine(book_id)
        st.success(f"Book {self.books_dict[book_id]['Title']} returned. Fine: ${fine}")
        del self.checked_out_books[book_id]

    def calculate_fine(self, book_id):
        if book_id not in self.books_dict:
            return 0
        book = self.books_dict[book_id]
        # Assume user reports minor damage for demonstration purposes
        fine = book["Minor Damage Fine"]
        return fine

# Instantiate the library system
library = LibrarySystem()

# Streamlit UI
st.title("Library System")

# Add member functionality
with st.expander("Add Member"):
    member_id = st.text_input("Enter Member ID")
    member_name = st.text_input("Enter Member Name")
    if st.button("Add Member"):
        if member_id and member_name:
            library.add_member(member_id, member_name)

# Display available books
with st.expander("Available Books"):
    library.display_books()

# Checkout a book functionality
with st.expander("Checkout Book"):
    member_id = st.text_input("Enter Member ID to Checkout Book")
    book_id = st.text_input("Enter Book ID to Checkout")
    if st.button("Checkout Book"):
        if member_id and book_id:
            library.checkout_book(member_id, book_id)

# Return a book functionality
with st.expander("Return Book"):
    member_id = st.text_input("Enter Member ID to Return Book")
    book_id = st.text_input("Enter Book ID to Return")
    if st.button("Return Book"):
        if member_id and book_id:
            library.return_book(member_id, book_id)
