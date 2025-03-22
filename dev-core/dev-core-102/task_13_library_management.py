class Book:
    def __init__(self, title, author, isbn, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available

    def book_info(self):
        print(f'"{self.title}" - {self.author}')

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Книга '{book.title}' найдена")
                return  
        print(f"Книга '{title}' не найдена")

    def list_available_books(self):
        if not self.books:
            print("В библиотеке нет книг.")
            return

        print("Список доступных книг в библиотеке:")
        for book in self.books:
            status = "Доступна" if book.is_available else "Выдана"
            print(f'"{book.title}" - {book.author} ({status})')

    def borrow_book(self, title, user):
        if len(user.borrowed_books_list) >= 2:
            print("Вы не можете взять больше 2 книг.")
            return
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.is_available = False
                    user.borrowed_books_list.append(book)
                    print(f"Книга '{book.title}' успешно взята пользователем {user.name}")
                else:
                    print(f"Книга '{book.title}' уже занята")
                return  
        print(f"Книга '{title}' не найдена")  

    def return_book(self, title, user):
        for book in user.borrowed_books_list:
            if book.title.lower() == title.lower():
                book.is_available = True
                user.borrowed_books_list.remove(book)
                print(f"Книга '{book.title}' снова доступна")
                return
        print(f"Книга '{title}' не найдена среди взятых книг пользователя {user.name}")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books_list = []  

    def borrowed_books(self):
        if not self.borrowed_books_list:
            print(f"{self.name} пока не взял(а) ни одной книги.")
            return
        print(f"Книги, которые взял(а) {self.name}:")
        for book in self.borrowed_books_list:
            print(f'"{book.title}" - {book.author}')

library = Library()
book1 = Book("1984", "George Orwell", "123456789")
book2 = Book("Master and Margarita", "Mikhael Bulgakov", "987654321")
book3 = Book("Crime and punishment", "Fyodor Dostoevsky", "456789123")
book4 = Book("Harry Potter", "J. K. Rowling", "123498765")
book5 = Book("Abay Zholy", "Mukhtar Auezov", "67891234")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)
library.add_book(book5)

library.list_available_books()

user_name = input("Введите имя пользователя: ")
user1 = User(user_name, 101)

while True:
    borrowed_book = input(f"{user_name}, введите название книги, которую хотите взять: ").strip()
    library.borrow_book(borrowed_book, user1)
    if len(user1.borrowed_books_list) >= 3:
        print("Можно взять максимум 3 книги")
        break
    next_operation = input("Хотите ли вы взять еще книги? (Напишите stop если нет): ")
    if next_operation.lower() == "stop":
        break

library.list_available_books()

user1.borrowed_books()

return_book_choice = (input("Хотите ли вы вернуть ОДНУ из книг: "))

if return_book_choice.strip().lower() == "yes":
    return_book = input("Введите название книги которую хотите вернуть: ")
    library.return_book(return_book, user1)
else:
    print("Спасибо за использование программы!")

library.list_available_books()
user1.borrowed_books()