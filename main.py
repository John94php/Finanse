import tkinter as tk
from tkinter import ttk
import sqlite3
from tkcalendar import Calendar


def save_expense(param, param1, param2, param3):
    print(param)
    # param - kwota
    # param1  - opis
    # param2 - kategoria
    # param3 - data dokonania wydatku

    print(param1)
    print(param2)
    print(param3)
    pass


class MyApp:
    def __init__(self, root):
        self.conn = sqlite3.connect("finanse.db")
        self.create_expenses_table()
        self.create_income_table()
        self.root = root
        self.root.title("Finanse")
        self.root.geometry('900x800')

        # Utwórz pasek nawigacyjny
        self.navbar = ttk.Frame(root)
        self.navbar.pack(side="top", fill="x")

        # Dodaj przyciski nawigacyjne do paska
        pages = ["Strona główna", "Dodaj wydatek", "Dodaj przychód", 'Wyjście']
        self.buttons = []
        for page in pages:
            button = ttk.Button(self.navbar, text=page, command=lambda p=page: self.show_page(p))
            button.pack(side="left", padx=5)
            self.buttons.append(button)

        self.content_frame = ttk.Frame(root)
        self.content_frame.pack(expand=True, fill="both")
        self.show_home_page()

    def show_page(self, page_name):
        if page_name == "Strona główna":
            self.show_home_page()
        elif page_name == "Dodaj wydatek":
            self.show_add_expense_page()
        elif page_name == "Dodaj przychód":
            self.show_add_income_page()
        elif page_name == "Wyjście":
            self.root.destroy()

    def show_home_page(self):
        self.clear_content()
        label = ttk.Label(self.content_frame, text="To jest strona główna.")

        label.pack(padx=10, pady=10)

    def show_add_expense_page(self):
        self.clear_content()
        # Utwórz formularz
        label_category = ttk.Label(self.content_frame, text="Kategoria:")
        label_category.pack(padx=10, pady=5)

        # Dodaj pole wyboru (Combobox) dla kategorii
        categories = ["Żywność", "Transport", "Zakupy", "Inne"]
        category_var = tk.StringVar()
        combo_category = ttk.Combobox(self.content_frame, textvariable=category_var, values=categories)
        combo_category.pack(padx=10, pady=5)

        label_description = ttk.Label(self.content_frame, text="Opis:")
        label_description.pack(padx=10, pady=5)
        entry_description = ttk.Entry(self.content_frame)
        entry_description.pack(padx=10, pady=5)

        label_date = ttk.Label(self.content_frame, text="Data dokonania wydatku:")
        label_date.pack(padx=10, pady=5)
        cal = Calendar(self.content_frame, selectmode='day',date_pattern="yyyy-mm-dd")
        cal.pack(padx=10, pady=5)

        label_amount = ttk.Label(self.content_frame, text="Kwota:")
        label_amount.pack(padx=10, pady=5)
        entry_amount = ttk.Entry(self.content_frame)
        entry_amount.pack(padx=10, pady=5)

        button_save = ttk.Button(self.content_frame, text="Zapisz",
                                 command=lambda: save_expense(entry_amount.get(), entry_description.get(),
                                                              category_var.get(), cal.get_date()))
        button_save.pack(pady=10)

    def show_add_income_page(self):
        self.clear_content()
        label = ttk.Label(self.content_frame, text="To jest strona dodawania przychodu.")
        label.pack(padx=10, pady=10)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def create_expenses_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS expences(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        date DATE,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
        )                
        ''')
        self.conn.commit()

    def create_income_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS income(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        description TEXT,
        date DATE,
        created DATETIME DEFAULT CURRENT_TIMESTAMP
        )                
        ''')
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
