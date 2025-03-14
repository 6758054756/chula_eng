Python 3.13.1 (v3.13.1:06714517797, Dec  3 2024, 14:00:22) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
import random

# Thai consonants and their names
consonants = [
    ("ก", "gor gai"),
    ("ข", "khor khai"),
    ("ค", "khor khwai"),
    ("ง", "ngor ngu"),
    ("จ", "jor jaan"),
    ("ฉ", "chor ching"),
    ("ช", "chor chang"),
    ("ซ", "sor so"),
    ("ญ", "yor ying"),
    ("ฎ", "dor cha-da"),
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")

        self.card_frame = tk.Frame(root, width=300, height=200, bg="white")
        self.card_frame.pack_propagate(False)
        self.card_frame.pack(pady=20)

        self.consonant_label = tk.Label(self.card_frame, text="", font=("Arial", 80), bg="white")
        self.consonant_label.pack(expand=True)

        self.flip_button = tk.Button(root, text="Flip Card", command=self.flip_card)
        self.flip_button.pack(pady=10)

        self.next_button = tk.Button(root, text="Next Card", command=self.next_card)
        self.next_button.pack(pady=10)

        self.current_consonant = None
        self.show_consonant()

    def show_consonant(self):
        self.current_consonant = random.choice(consonants)
        self.consonant_label.config(text=self.current_consonant[0])

    def flip_card(self):
        if self.consonant_label.cget("text") == self.current_consonant[0]:
            self.consonant_label.config(text=self.current_consonant[1])
        else:
            self.consonant_label.config(text=self.current_consonant[0])

    def next_card(self):
        self.show_consonant()

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

SyntaxError: multiple statements found while compiling a single statement
import tkinter as tk
import random

# Thai consonants and their names
consonants = [
    ("ก", "gor gai"),
    ("ข", "khor khai"),
    ("ค", "khor khwai"),
    ("ง", "ngor ngu"),
    ("จ", "jor jaan"),
    ("ฉ", "chor ching"),
    ("ช", "chor chang"),
    ("ซ", "sor so"),
    ("ญ", "yor ying"),
    ("ฎ", "dor cha-da"),
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")

        self.card_frame = tk.Frame(root, width=300, height=200, bg="white")
        self.card_frame.pack_propagate(False)
        self.card_frame.pack(pady=20)

        self.consonant_label = tk.Label(self.card_frame, text="", font=("Arial", 80), bg="white")
...         self.consonant_label.pack(expand=True)
... 
...         self.flip_button = tk.Button(root, text="Flip Card", command=self.flip_card)
...         self.flip_button.pack(pady=10)
... 
...         self.next_button = tk.Button(root, text="Next Card", command=self.next_card)
...         self.next_button.pack(pady=10)
... 
...         self.current_consonant = None
...         self.show_consonant()
... 
...     def show_consonant(self):
...         self.current_consonant = random.choice(consonants)
...         self.consonant_label.config(text=self.current_consonant[0])
... 
...     def flip_card(self):
...         if self.consonant_label.cget("text") == self.current_consonant[0]:
...             self.consonant_label.config(text=self.current_consonant[1])
...         else:
...             self.consonant_label.config(text=self.current_consonant[0])
... 
...     def next_card(self):
...         self.show_consonant()
... 
... if __name__ == "__main__":
...     root = tk.Tk()
...     app = FlashcardApp(root)
...     root.mainloop()
... 
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> python thai_flashcards.py
... 
SyntaxError: invalid syntax
>>> python thai_flashcards.py
... 
SyntaxError: invalid syntax
