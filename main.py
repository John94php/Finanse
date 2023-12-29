import tkinter as tk
from tkinter import ttk


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Finanse")
        self.root.geometry('900x400')

        # Utwórz pasek nawigacyjny
        self.navbar = ttk.Frame(root)
        self.navbar.pack(side="top", fill="x")

        # Dodaj przyciski nawigacyjne do paska
        pages = ["Strona główna", "Dodaj wydatek", "Dodaj przychód"]
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

    def show_home_page(self):
        self.clear_content()
        label = ttk.Label(self.content_frame, text="To jest strona główna.")
        label.pack(padx=10, pady=10)

    def show_add_expense_page(self):
        self.clear_content()
        label = ttk.Label(self.content_frame, text="To jest strona dodawania wydatku.")
        label.pack(padx=10, pady=10)

    def show_add_income_page(self):
        self.clear_content()
        label = ttk.Label(self.content_frame, text="To jest strona dodawania przychodu.")
        label.pack(padx=10, pady=10)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
