# Quiz App

A desktop **True/False Quiz Application** built with Python and Tkinter.

The application retrieves quiz questions dynamically from the Open Trivia Database API and presents them through an interactive graphical user interface. It keeps track of the user's progress and score and provides immediate visual feedback after each answer.

This project was developed as part of **Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp** and further extended and organized while learning Python, object-oriented programming, GUI development, and working with external APIs.

---

## Preview
<p align="center">
 <img src="images/QuizzMaster_snapshot.png" />
</p>

---

## Features

* True/False quiz questions
* Questions retrieved dynamically from the **Open Trivia Database API**
* Interactive graphical user interface built with Tkinter
* Score tracking
* Question progress indicator
* Immediate visual feedback for correct and incorrect answers
* **New Quiz functionality** to start a fresh quiz after completion
* Separate modules for application components
* Object-oriented quiz logic
* Custom True/False button graphics

---

## Built With

![Python](https://img.shields.io/badge/Python-3.9.1-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-FFCC00?style=for-the-badge)
![OOP](https://img.shields.io/badge/Concept-Object--Oriented%20Programming-6A5ACD?style=for-the-badge)


## External API

Quiz questions are provided by the **Open Trivia Database**:

[Open Trivia Database](https://opentdb.com)

The API provides the question data used by the application, allowing a new set of questions to be retrieved rather than relying on a fixed collection stored directly in the application.

---

## Project Structure

```text
Quiz-App/
│
├── images/
│   ├── true.png
│   ├── false.png
│   └── QuizzMaster_snapshot.png
│
├── main.py
├── data.py
├── question_model.py
├── quiz_brain.py
├── ui.py
├── requirements.txt
└── README.md
```

### `main.py`

The main entry point of the application.

It initializes the quiz and connects the quiz logic with the graphical user interface.

### `data.py`

Handles retrieving the quiz questions from the **Open Trivia Database API**.

The API response is processed so that the question data can be used by the quiz application.

### `question_model.py`

Defines the `Question` class.

Each question object contains the question text and its corresponding correct answer.

### `quiz_brain.py`

Contains the `QuizBrain` class and manages the core quiz logic.

Responsibilities include:

* Keeping track of the current question
* Retrieving questions
* Checking answers
* Updating the score
* Determining when the quiz is finished

### `ui.py`

Contains the graphical user interface built with Tkinter.

Responsibilities include:

* Displaying questions
* Displaying the current score
* Showing question progress
* Handling True/False button clicks
* Providing visual feedback
* Displaying the final result
* Providing the **New Quiz** functionality

### `images/`

Contains the graphical assets used by the application.

---

## Getting Started

### Prerequisites

Make sure you have **Python 3** installed on your computer.

You can check your Python installation with:

```bash
python --version
```

The application uses **Tkinter**, which is included with most standard Python installations.

An internet connection is required because quiz questions are retrieved from the Open Trivia Database API.

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/sylviawg/quizz-master-app.git
```

### 2. Navigate to the project directory

```bash
cd quizz-master-app
```

### 3. Run the application

```bash
python main.py
```

The quiz window should open automatically.

---

## How to Play

1. Start the application.
2. A question retrieved from the Open Trivia Database is displayed.
3. Select **True** or **False**.
4. The application immediately indicates whether the answer was correct.
5. Your score and question progress are updated.
6. Continue until all questions have been answered.
7. Your final score is displayed when the quiz is complete.
8. Click **New Quiz** to retrieve a new set of questions and start another quiz.

---

## New Quiz Functionality

After completing a quiz, the application provides a **New Quiz** button.

Selecting this button resets the relevant quiz state and retrieves a new set of questions from the Open Trivia Database API.

This was an additional feature added to extend the original project functionality and make the application reusable without having to restart the program.

---

## Concepts Practiced

This project was an opportunity to practice several Python concepts:

* **Object-Oriented Programming**

  * Classes
  * Objects
  * Methods
  * Attributes

* **Modular programming**

  * Splitting the application into multiple Python files
  * Importing and using classes from other modules

* **Tkinter GUI development**

  * Windows
  * Labels
  * Buttons
  * Canvas
  * Event handling

* **Program state**

  * Tracking the current question
  * Tracking the score
  * Managing quiz progress

* **Python data structures**

  * Lists
  * Dictionaries

* **Functions and conditional logic**

---

## Project Architecture

The application separates the **data**, **quiz logic**, and **user interface** into different modules.

```text
             ┌─────────────┐
             │   main.py   │
             └──────┬──────┘
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
   ┌─────────────┐     ┌─────────────┐
   │ quiz_brain  │     │     ui      │
   │    .py      │     │    .py      │
   └──────┬──────┘     └──────┬──────┘
          │                   │
          ▼                   │
   ┌─────────────┐            │
   │question_model│           │
   │    .py      │            │
   └──────┬──────┘            │
          │                   │
          └─────────┬─────────┘
                    ▼
              ┌───────────┐
              │  data.py  │
              └───────────┘
```

This separation makes the application easier to understand, maintain, and extend.

---

## Future Improvements

Possible improvements for future versions include:

* [ ] Add multiple quiz categories
* [ ] Add different difficulty levels
* [ ] Allow the user to choose the number of questions
* [ ] Add a timer
* [ ] Add a high-score system
* [ ] Add more question types
* [ ] Allow users to create their own question sets
* [ ] Improve the visual design and responsiveness

---

## Learning Journey

This project is part of my ongoing journey learning Python.

While following the original course project, I used the opportunity to explore how the different components of a Python application can be separated into dedicated modules.

The project helped me move beyond writing everything in a single script and gain practical experience with **object-oriented programming, modular code organization, and GUI development**.

---

## Credits

This project was originally inspired by the **100 Days of Code: The Complete Python Pro Bootcamp** by **Angela Yu**.

The application was developed as a learning project and subsequently organized and customized while practicing Python.

---

## License

This project was created for educational and portfolio purposes.
