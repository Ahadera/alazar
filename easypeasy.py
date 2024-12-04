import tkinter as tk
from tkinter import messagebox

class LibraryMasterSystem:
    def __init__(self):
           self.members = {}
           self.checked_out_books = {}
           self.books_dict_wide_choices = {
    "1984": {"Title": "1984", "Author": "George Orwell", "Minor Damage Fine": 10, "Severe Damage Fine": 35, "Status": "Available", "Due Date": None},
    "Moby-Dick": {"Title": "Moby-Dick", "Author": "Herman Melville", "Minor Damage Fine": 15, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "To Kill a Mockingbird": {"Title": "To Kill a Mockingbird", "Author": "Harper Lee", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "Pride and Prejudice": {"Title": "Pride and Prejudice", "Author": "Jane Austen", "Minor Damage Fine": 10, "Severe Damage Fine": 40, "Status": "Available", "Due Date": None},
    "The Catcher in the Rye": {"Title": "The Catcher in the Rye", "Author": "J.D. Salinger", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "The Great Gatsby": {"Title": "The Great Gatsby", "Author": "F. Scott Fitzgerald", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "Jane Eyre": {"Title": "Jane Eyre", "Author": "Charlotte Brontë", "Minor Damage Fine": 11, "Severe Damage Fine": 42, "Status": "Available", "Due Date": None},
    "The Lord of the Rings": {"Title": "The Lord of the Rings", "Author": "J.R.R. Tolkien", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "The Hobbit": {"Title": "The Hobbit", "Author": "J.R.R. Tolkien", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "Crime and Punishment": {"Title": "Crime and Punishment", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "War and Peace": {"Title": "War and Peace", "Author": "Leo Tolstoy", "Minor Damage Fine": 25, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "Anna Karenina": {"Title": "Anna Karenina", "Author": "Leo Tolstoy", "Minor Damage Fine": 22, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "Don Quixote": {"Title": "Don Quixote", "Author": "Miguel de Cervantes", "Minor Damage Fine": 18, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "The Brothers Karamazov": {"Title": "The Brothers Karamazov", "Author": "Fyodor Dostoevsky", "Minor Damage Fine": 21, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "The Picture of Dorian Gray": {"Title": "The Picture of Dorian Gray", "Author": "Oscar Wilde", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "The Odyssey": {"Title": "The Odyssey", "Author": "Homer", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "The Iliad": {"Title": "The Iliad", "Author": "Homer", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "The Divine Comedy": {"Title": "The Divine Comedy", "Author": "Dante Alighieri", "Minor Damage Fine": 20, "Severe Damage Fine": 70, "Status": "Available", "Due Date": None},
    "Frankenstein": {"Title": "Frankenstein", "Author": "Mary Shelley", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "Dracula": {"Title": "Dracula", "Author": "Bram Stoker", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "The Adventures of Huckleberry Finn": {"Title": "The Adventures of Huckleberry Finn", "Author": "Mark Twain", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "Catch-22": {"Title": "Catch-22", "Author": "Joseph Heller", "Minor Damage Fine": 16, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "Slaughterhouse-Five": {"Title": "Slaughterhouse-Five", "Author": "Kurt Vonnegut", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "The Road": {"Title": "The Road", "Author": "Cormac McCarthy", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "Beloved": {"Title": "Beloved", "Author": "Toni Morrison", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "The Color Purple": {"Title": "The Color Purple", "Author": "Alice Walker", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "Of Mice and Men": {"Title": "Of Mice and Men", "Author": "John Steinbeck", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "East of Eden": {"Title": "East of Eden", "Author": "John Steinbeck", "Minor Damage Fine": 16, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "The Grapes of Wrath": {"Title": "The Grapes of Wrath", "Author": "John Steinbeck", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "The Shining": {"Title": "The Shining", "Author": "Stephen King", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "Carrie": {"Title": "Carrie", "Author": "Stephen King", "Minor Damage Fine": 16, "Severe Damage Fine": 60, "Status": "Available", "Due Date": None},
    "It": {"Title": "It", "Author": "Stephen King", "Minor Damage Fine": 20, "Severe Damage Fine": 75, "Status": "Available", "Due Date": None},
    "The Stand": {"Title": "The Stand", "Author": "Stephen King", "Minor Damage Fine": 18, "Severe Damage Fine": 65, "Status": "Available", "Due Date": None},
    "The Dark Tower": {"Title": "The Dark Tower", "Author": "Stephen King", "Minor Damage Fine": 22, "Severe Damage Fine": 80, "Status": "Available", "Due Date": None},
    "The Girl with the Dragon Tattoo": {"Title": "The Girl with the Dragon Tattoo", "Author": "Stieg Larsson", "Minor Damage Fine": 15, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
    "The Hunger Games": {"Title": "The Hunger Games", "Author": "Suzanne Collins", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "Divergent": {"Title": "Divergent", "Author": "Veronica Roth", "Minor Damage Fine": 12, "Severe Damage Fine": 45, "Status": "Available", "Due Date": None},
    "The Maze Runner": {"Title": "The Maze Runner", "Author": "James Dashner", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "The Handmaid's Tale": {"Title": "The Handmaid's Tale", "Author": "Margaret Atwood", "Minor Damage Fine": 14, "Severe Damage Fine": 50, "Status": "Available", "Due Date": None},
    "Brave New World": {"Title": "Brave New World", "Author": "Aldous Huxley", "Minor Damage Fine": 16, "Severe Damage Fine": 55, "Status": "Available", "Due Date": None},
}

    def check_out_book_from_the_collection(self, book_title, member_name, due_date):
        if book_title in self.books_dict_wide_choices:
            book = self.books_dict_wide_choices[book_title]
            if book["Status"] == "Available":
                book["Status"] = "Checked Out"
                book["Due Date"] = due_date
                if member_name not in self.members:
                    self.members[member_name] = []
                self.members[member_name].append(book_title)
                messagebox.showinfo(
                    "Success",
                    f"{book_title} has been checked out by {member_name}. Due date: {due_date}",
                )
            else:
                messagebox.showerror("Error", f"{book_title} is already checked out.")
        else:
            messagebox.showerror("Error", f"Book titled {book_title} not found.")

    def returning_loaned_book_from_the_collection(self, book_title, member_name):
        if member_name in self.members:
            if book_title in self.members[member_name]:
                book = self.books_dict_wide_choices[book_title]
                book["Status"] = "Available"
                book["Due Date"] = None
                self.members[member_name].remove(book_title)
                messagebox.showinfo(
                    "Success", f"{book_title} has been returned by {member_name}."
                )
            else:
                messagebox.showerror(
                    "Error", f"{book_title} was not checked out by {member_name}."
                )
        else:
            messagebox.showerror("Error", f"Member {member_name} not found.")

    def viewing_books_in_the_collection(self):
        available_books = [
            f"Title: {book['Title']}, Author: {book['Author']}, Minor Damage Fine: ${book['Minor Damage Fine']}, Severe Damage Fine: ${book['Severe Damage Fine']}"
            for book in self.books_dict_wide_choices.values()
            if book["Status"] == "Available"
        ]
        messagebox.showinfo(
            "Available Books",
            "\n".join(available_books) if available_books else "No books available.",
        )


def creating_the_Library_interface():
    library = LibraryMasterSystem()

    def checkout():
        book_title = book_entry.get()
        member_name = member_entry.get()
        due_date = due_date_entry.get()
        library.check_out_book_from_the_collection(book_title, member_name, due_date)

    def return_book_to_collection():
        book_title = book_entry.get()
        member_name = member_entry.get()
        library.returning_loaned_book_from_the_collection(book_title, member_name)

    def view_books():
        library.viewing_books_in_the_collection()

    root = tk.Tk()
    root.title("Library Master Management System")

    tk.Label(root, text="Book Title:").grid(row=0, column=0)
    book_entry = tk.Entry(root)
    book_entry.grid(row=0, column=1)

    
    tk.Label(root, text="Member Name:").grid(row=1, column=0)
    member_entry = tk.Entry(root)
    member_entry.grid(row=1, column=1)

    
    tk.Label(root, text="Due Date (YYYY-MM-DD):").grid(row=2, column=0)
    due_date_entry = tk.Entry(root)
    due_date_entry.grid(row=2, column=1)

 
    tk.Button(root, text="Check Out Book", command=checkout).grid(row=3, column=0)
    tk.Button(root, text="Return Book", command=return_book_to_collection ).grid(row=3, column=1)
    tk.Button(root, text="View Available Books", command=view_books).grid(
        row=4, column=0, columnspan=2
    )

    root.mainloop()


creating_the_Library_interface()
    