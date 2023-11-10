class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")
        print(f"Status: {'Checked Out' if self.checked_out else 'Available'}")

    def check_out(self):
        if not self.checked_out:
            print(f"{self.title} is now checked out.")
            self.checked_out = True
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.checked_out:
            print(f"{self.title} has been returned.")
            self.checked_out = False
        else:
            print(f"{self.title} is not checked out.")


class Book(LibraryItem):
    def __init__(self, title, author, item_id, genre):
        super().__init__(title, author, item_id)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")
        print("")


class DVD(LibraryItem):
    def __init__(self, title, director, item_id, duration):
        super().__init__(title, director, item_id)
        self.director = director
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}")
        print(f"Duration: {self.duration} minutes")
        print("")


class Magazine(LibraryItem):
    def __init__(self, title, publisher, item_id, issue_number):
        super().__init__(title, publisher, item_id)
        self.publisher = publisher
        self.issue_number = issue_number

    def display_info(self):
        super().display_info()
        print(f"Publisher: {self.publisher}")
        print(f"Issue Number: {self.issue_number}")
        print("")

# Example Usage:
book = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", item_id="B001", genre="Classic")
book.display_info()
book.check_out()
book.return_item()

dvd = DVD(title="Inception", director="Christopher Nolan", item_id="D001", duration=148)
dvd.display_info()
dvd.check_out()

magazine = Magazine(title="National Geographic", publisher="National Geographic Society", item_id="M001", issue_number=255)
magazine.display_info()
magazine.check_out()
