import tkinter as tk
import random
from tkinter import messagebox

# List of Thai consonants and their names
consonants = [
    ("ก", "gor kai"),
    ("ข", "khor khai"),
    ("ฃ", "khor khwua"),
    ("ค", "khor khai"),
    ("ฅ", "khor khon"),
    ("ฆ", "khor raakhang"),
    ("ง", "ngor ngoo"),
    ("จ", "jor jaan"),
    ("ฉ", "chor ching"),
    ("ช", "chor chang"),
    ("ซ", "sor soo"),
    ("ฌ", "chor chaa"),
    ("ญ", "yor ying"),
    ("ฎ", "dor chaada"),
    ("ฏ", "tor paak"),
    ("ฐ", "thor than"),
    ("ฑ", "thor phuuthao"),
    ("ฒ", "thor moohok"),
    ("ณ", "nor naan"),
    ("ด", "dor dek"),
    ("ต", "tor tao"),
    ("ถ", "thor thong"),
    ("ท", "thor thahaan"),
    ("ธ", "thor tham"),
    ("น", "nor nooa"),
    ("บ", "bor bai mai"),
    ("ป", "por plaa"),
    ("ผ", "phor phuung"),
    ("ฝ", "for faa"),
    ("พ", "phor phaa"),
    ("ฟ", "for fang"),
    ("ภ", "phor samphao"),
    ("ม", "mor maa"),
    ("ย", "yor yak"),
    ("ร", "ror ruu"),
    ("ล", "lor ling"),
    ("ว", "wor waaen"),
    ("ศ", "sor saket"),
    ("ษ", "sor ruek"),
    ("ส", "sor sua"),
    ("ห", "hor heep"),
    ("ฬ", "lor juul"),
    ("อ", "or ang"),
    ("ฮ", "hor nokhak")
]

# Initialize the window
root = tk.Tk()
root.title("Thai Consonant Flashcards")

# Set window size
root.geometry("400x300")

# Create a label to show the card content
card_label = tk.Label(root, text="", font=("Arial", 40), width=10, height=5, relief="solid")
card_label.pack(pady=50)

# Function to flip the card
def flip_card():
    global show_name
    if show_name:
        card_label.config(text=consonant_name)
    else:
        card_label.config(text=consonant)
    show_name = not show_name

# Function to show a new consonant
def new_card():
    global consonant, consonant_name, show_name
    consonant, consonant_name = random.choice(consonants)
    show_name = False
    card_label.config(text=consonant)

# Function to save the current card to a file
def save_card():
    global consonant, consonant_name, show_name
    card_to_save = consonant_name if show_name else consonant
    try:
        with open("flashcard.txt", "a", encoding="utf-8") as file:
            file.write(f"{card_to_save}\n")
        messagebox.showinfo("Success", f"Card '{card_to_save}' saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Initial state
show_name = False
new_card()

# Buttons to flip the card, show a new one, and save the card
flip_button = tk.Button(root, text="Flip", font=("Arial", 14), command=flip_card)
flip_button.pack(side=tk.LEFT, padx=20)

new_button = tk.Button(root, text="New Card", font=("Arial", 14), command=new_card)
new_button.pack(side=tk.RIGHT, padx=20)

save_button = tk.Button(root, text="Save", font=("Arial", 14), command=save_card)
save_button.pack(side=tk.BOTTOM, pady=20)

# Run the Tkinter main loop
root.mainloop()
