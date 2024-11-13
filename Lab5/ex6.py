class LibraryItem:
    """Base class for all library items"""

    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_checked_out = False

    def check_out(self):
        """Mark the item as checked out"""
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        """Mark the item as returned"""
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

    def display_info(self):
        """Display basic information about the item"""
        status = "Checked Out" if self.is_checked_out else "Available"
        return f"Title: {self.title}, ID: {self.item_id}, Status: {status}"


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def display_info(self):
        """Override to include book-specific information"""
        return super().display_info() + f", Author: {self.author}, Pages: {self.pages}"


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration  # Duration in minutes

    def display_info(self):
        """Override to include DVD-specific information"""
        return super().display_info() + f", Director: {self.director}, Duration: {self.duration} minutes"


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue, publisher):
        super().__init__(title, item_id)
        self.issue = issue
        self.publisher = publisher

    def display_info(self):
        """Override to include magazine-specific information"""
        return super().display_info() + f", Issue: {self.issue}, Publisher: {self.publisher}"


# Example usage
book = Book(title="The Great Gatsby", item_id="B001", author="F. Scott Fitzgerald", pages=180)
dvd = DVD(title="Inception", item_id="D001", director="Christopher Nolan", duration=148)
magazine = Magazine(title="National Geographic", item_id="M001", issue="March 2023", publisher="National Geographic Society")

# Display information and check out/return items
print(book.display_info())
book.check_out()
book.return_item()

print(dvd.display_info())
dvd.check_out()
dvd.return_item()

print(magazine.display_info())
magazine.check_out()
magazine.return_item()
