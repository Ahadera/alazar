import streamlit as st

class LibrarySystem:
    def __init__(self):
           self.members = {}
           self.checked_out_books = {}
           self.books_dict = {
  
    "1": {"Title": "1984", "Author": "George Orwell", "Minor Damage Fine": 10, "Severe Damage Fine": 35, "Status": "Available", "Due Date": None},
    "2": {"Title": "Moby-Dick", "Author": "Herman Melville", "Minor Damage Fine": 15, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "3": {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "4": {"Title": "Pride and Prejudice", "Author": "Jane Austen", "Minor Damage Fine": 10, "Severe Damage Fine": 40, "Status": "Available", "Due Date": None},
    "5": {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "6": {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "7": {"Title": "Jane Eyre", "Author": "Charlotte Brontë", "Minor Damage Fine": 11, "Severe Damage Fine": 42, "Status": "Available", "Due Date": None},
    "8": {"Title": "The Lord of the Rings", "Author": "J.R.R. Tolkien", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "9": {"Title": "The Hobbit", "Author": "J.R.R. Tolkien", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "10": {"Title": "Crime and Punishment", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "11": {"Title": "War and Peace", "Author": "Leo Tolstoy", "Minor Damage Fine": 25, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "12": {"Title": "Anna Karenina", "Author": "Leo Tolstoy", "Minor Damage Fine": 22, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "13": {"Title": "Don Quixote", "Author": "Miguel de Cervantes", "Minor Damage Fine": 18, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "14": {"Title": "The Brothers Karamazov", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 21, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "15": {"Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "16": {"Title": "The Odyssey", "Author": "Homer", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "17": {"Title": "The Iliad", "Author": "Homer", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "18": {"Title": "The Divine Comedy", "Author": "Dante Alighieri", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "19": {"Title": "Frankenstein", "Author": "Mary Shelley", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "20": {"Title": "Dracula", "Author": "Bram Stoker", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "21": {"Title": "The Adventures of Huckleberry Finn", "Author": "Mark Twain", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "22": {"Title": "Catch-22", "Author": "Joseph Heller", "Minor Damage Fine": 16, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "23": {"Title": "Slaughterhouse-Five", "Author": "Kurt Vonnegut", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "24": {"Title": "The Road", "Author": "Cormac McCarthy", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "25": {"Title": "Beloved", "Author": "Toni Morrison", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "26": {"Title": "The Color Purple", "Author": "Alice Walker", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "27": {"Title": "Of Mice and Men", "Author": "John Steinbeck", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "28": {"Title": "East of Eden", "Author": "John Steinbeck", "Minor Damage Fine": 16, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "29": {"Title": "The Grapes of Wrath", "Author": "John Steinbeck", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "30": {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "31": {"Title": "The Shining", "Author": "Stephen King", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "32": {"Title": "Carrie", "Author": "Stephen King", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "33": {"Title": "It", "Author": "Stephen King", "Minor Damage Fine": 20, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "34": {"Title": "The Stand", "Author": "Stephen King", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "35": {"Title": "The Dark Tower", "Author": "Stephen King", "Minor Damage Fine": 22, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "36": {"Title": "The Girl with the Dragon Tattoo", "Author": "Stieg Larsson", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "37": {"Title": "The Hunger Games", "Author": "Suzanne Collins", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "38": {"Title": "Divergent", "Author": "Veronica Roth", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "39": {"Title": "The Maze Runner", "Author": "James Dashner", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "40": {"Title": "The Handmaid's Tale", "Author": "Margaret Atwood", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "41": {"Title": "The Left Hand of Darkness", "Author": "Ursula K. Le Guin", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "42": {"Title": "Brave New World", "Author": "Aldous Huxley", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "43": {"Title": "Fahrenheit 451", "Author": "Ray Bradbury", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "44": {"Title": "A Clockwork Orange", "Author": "Anthony Burgess", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "45": {"Title": "Neuromancer", "Author": "William Gibson", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "46": {"Title": "The Stranger", "Author": "Albert Camus", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "47": {"Title": "The Trial", "Author": "Franz Kafka", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "48": {"Title": "The Plague", "Author": "Albert Camus", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "49": {"Title": "The Metamorphosis", "Author": "Franz Kafka", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "50": {"Title": "The Brothers Karamazov", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "51": {"Title": "The Scarlet Letter", "Author": "Nathaniel Hawthorne", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "52": {"Title": "Frankenstein", "Author": "Mary Shelley", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "53": {"Title": "Wuthering Heights", "Author": "Emily Brontë", "Minor Damage Fine": 13, "Severe Damage Fine": 48, "Status": "Available", "Due Date": None},
    "54": {"Title": "Rebecca", "Author": "Daphne du Maurier", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "55": {"Title": "A Tale of Two Cities", "Author": "Charles Dickens", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "56": {"Title": "Les Misérables", "Author": "Victor Hugo", "Minor Damage Fine": 22, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "57": {"Title": "Great Expectations", "Author": "Charles Dickens", "Minor Damage Fine": 17, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "58": {"Title": "Oliver Twist", "Author": "Charles Dickens", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "59": {"Title": "Dr. Jekyll and Mr. Hyde", "Author": "Robert Louis Stevenson", "Minor Damage Fine": 13, "Severe Damage Fine": 48, "Status": "Available", "Due Date": None},
    "60": {"Title": "Treasure Island", "Author": "Robert Louis Stevenson", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "61": {"Title": "The Call of the Wild", "Author": "Jack London", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "62": {"Title": "White Fang", "Author": "Jack London", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "63": {"Title": "The Sun Also Rises", "Author": "Ernest Hemingway", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "64": {"Title": "A Farewell to Arms", "Author": "Ernest Hemingway", "Minor Damage Fine": 17, "Severe Damage Fine": 62, "Status": "Available", "Due Date": None},
    "65": {"Title": "The Old Man and the Sea", "Author": "Ernest Hemingway", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "66": {"Title": "For Whom the Bell Tolls", "Author": "Ernest Hemingway", "Minor Damage Fine": 19, "Severe Damage Fine": 68, "Status": "Available", "Due Date": None},
    "67": {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "68": {"Title": "This Side of Paradise", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "69": {"Title": "Tender is the Night", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 17, "Severe Damage Fine": 62, "Status": "Available", "Due Date": None},
    "70": {"Title": "The Beautiful and the Damned", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "71": {"Title": "The Fountainhead", "Author": "Ayn Rand", "Minor Damage Fine": 22, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "72": {"Title": "Atlas Shrugged", "Author": "Ayn Rand", "Minor Damage Fine": 24, "Severe Damage Fine": 90, "Status": "Available", "Due Date": None},
    "73": {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "74": {"Title": "The Bell Jar", "Author": "Sylvia Plath", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "75": {"Title": "One Flew Over the Cuckoo's Nest", "Author": "Ken Kesey", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "76": {"Title": "The Road", "Author": "Cormac McCarthy", "Minor Damage Fine": 20, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "77": {"Title": "No Country for Old Men", "Author": "Cormac McCarthy", "Minor Damage Fine": 19, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "78": {"Title": "Blood Meridian", "Author": "Cormac McCarthy", "Minor Damage Fine": 20, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "79": {"Title": "The Godfather", "Author": "Mario Puzo", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "80": {"Title": "The Godfather Returns", "Author": "Mark Winegardner", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "81": {"Title": "The Silence of the Lambs", "Author": "Thomas Harris", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "82": {"Title": "Red Dragon", "Author": "Thomas Harris", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "83": {"Title": "Hannibal", "Author": "Thomas Harris", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "84": {"Title": "The Girl with the Dragon Tattoo", "Author": "Stieg Larsson", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "85": {"Title": "The Girl Who Played with Fire", "Author": "Stieg Larsson", "Minor Damage Fine": 17, "Severe Damage Fine": 62, "Status": "Available", "Due Date": None},
    "86": {"Title": "The Girl Who Kicked the Hornet's Nest", "Author": "Stieg Larsson", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "87": {"Title": "The Help", "Author": "Kathryn Stockett", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "88": {"Title": "The Secret Life of Bees", "Author": "Sue Monk Kidd", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "89": {"Title": "The Alchemist", "Author": "Paulo Coelho", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "90": {"Title": "The Zahir", "Author": "Paulo Coelho", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None}
    }

def check_out_book(self, book_title, member_name, due_date):
        if book_title in self.books_dict:
            book = self.books_dict[book_title]
            if book["Status"] == "Available":
                book["Status"] = "Checked Out"
                book["Due Date"] = due_date
                if member_name not in self.members:
                    self.members[member_name] = []  # Add the member if they don't exist
                self.members[member_name].append(book_title)  # Assign the book to the member
                st.write(f"{book_title} has been checked out by {member_name}. Due date: {due_date}")
            else:
                st.write(f"{book_title} is already checked out.")
        else:
            st.write(f"Book titled {book_title} not found.")
    
def return_book(self, book_title, member_name):
        if member_name in self.members:
            if book_title in self.members[member_name]:
                book = self.books_dict[book_title]
                book["Status"] = "Available"
                book["Due Date"] = None
                self.members[member_name].remove(book_title)  # Remove the book from the member
                st.write(f"{book_title} has been returned by {member_name}.")
            else:
                st.write(f"{book_title} was not checked out by {member_name}.")
        else:
            st.write(f"Member {member_name} not found.")
    
def view_books(self):
        st.write("Available Books:")
        for title, book in self.books_dict.items():
            if book["Status"] == "Available":
                st.write(f"Title: {book['Title']}, Author: {book['Author']}, Minor Damage Fine: ${book['Minor Damage Fine']}, Severe Damage Fine: ${book['Severe Damage Fine']}")

# Example Usage
library = LibrarySystem()

# Checking out a book
library.check_out_book("1984", "John Doe", "2024-12-15")
library.check_out_book("Moby-Dick", "Jane Smith", "2024-12-20")

# Returning a book
library.return_book("1984", "John Doe")

# Viewing available books
library.view_books()
