

# 🟩 Wordle: Python OOP Implementation

This project is a custom version of the popular word-guessing game **Wordle**, developed for the **Advanced Programming Concepts (APC)** course. It focuses on utilizing **Object-Oriented Programming (OOP)** to create a modular and scalable gaming experience.

## 🎮 Game Features

* 
**Two Game Modes:** Includes a **Normal Mode** for standard play and a **Daily Mode** where everyone globally plays the same word based on the date.


* 
**Customizable Settings:** A dedicated settings menu allows players to toggle between 5 or 6-letter words and set the difficulty to Easy or Difficult.


* 
**Interactive Feedback:** Uses a color-coded scoring system where 1 (Green) is a correct match, 2 (Yellow) is the right letter in the wrong spot, and 0 (Red/Gray) is an incorrect letter.


* 
**Statistics & Persistence:** Tracks user streaks, win/loss history, and performance statistics across sessions.


* 
**Validation:** Guesses are checked against a dictionary to ensure only valid 5 or 6-letter words are accepted.



---

## 🛠️ Technical Implementation

The project is built to meet specific academic criteria for **OOP** and clean code organization:

* **OOP Principles:** Implements concrete objects (Game, Player, WordManager) with structured relations to avoid redundancy.
* **Composition-Based:** Prioritizes composition over inheritance to ensure modularity and reduce dependency issues.
* 
**Single Command Execution:** In accordance with course requirements, the entire application runs via the `Main.py` file.


* **Centralized Utilities:** Uses a `Constants` class for dialogue and a `Utilities` class for shared methods like colored console output.

---

## 👥 Team & Responsibilities

The workload was divided among the group to ensure equal contribution:

* 
**Game Logic Developer:** Core mechanics, word checking, and feedback systems.


* 
**UI/UX Developer:** Interface design (TUI/GUI) and user experience.


* 
**Word Manager:** Loading dictionaries, validating words, and managing difficulty tiers.


* 
**Testing & Scoring Lead:** Unit testing and statistical tracking.


* 
**Report Writing:** Managed by Patri and Abbas.



---

## 🚀 How to Run

1. **Clone the repository:**
```bash
git clone [https://github.com/sidrabilal71/WordleAPCProject]

```


2. **Install dependencies:**
```bash
pip install colorama

```


3. **Execute the game:**
```bash
python Main.py

```



---

Would you like me to help you draft the **5-7 page PDF report** or the **intermediate progress report** due on May 1st?
