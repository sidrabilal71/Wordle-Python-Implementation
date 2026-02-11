

# 🟩 Wordle: Python OOP Implementation

This project is a custom version of the popular word-guessing game **Wordle**, developed for the **Advanced Programming Concepts (APC)** course. It focuses on utilizing **Object-Oriented Programming (OOP)** to create a modular and scalable gaming experience.

## 🎮 Game Features

* **Normal Mode:** Play with a randomly selected word at any time.
* **Daily Mode:** Play the "Word of the Day"—the same word is generated globally for all players based on the date.
* **Customizable Settings:** A dedicated menu to change word length (5 or 6 letters) and difficulty levels (Easy or Difficult).
* **Real-time Feedback:** * 🟩 **Green (1):** Correct letter in the correct position.
* 🟨 **Yellow (2):** Correct letter in the wrong position.
* ⬜ **Gray/Red (0):** Letter is not in the word.


* **Player Statistics:** Tracks win/loss notifications, current streaks, and past performance.
* **Validation:** Only accepts valid dictionary words that match the selected length.

---

## 🛠️ Technical Design

The project is built to meet specific academic criteria for **OOP** and clean code organization:

* **Object-Oriented Architecture:** Implements concrete classes (Game, Player, WordManager) to manage game state and relations.
* **Composition-Based:** Prioritizes composition to ensure modularity and reduce dependency issues between classes.
* **Functional Programming:** Utilizes list comprehensions and filters for efficient word list management and validation.
* **Single Entry Point:** The entire application runs via a single command through the `Main.py` file.



---

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/sidrabilal71/WordleAPCProject

```


2. **Install dependencies:**
```bash
pip install colorama

```


3. **Run the game:**
```bash
python Main.py

```



---

Would you like me to help you draft the **written PDF report** (5-7 pages) next?
