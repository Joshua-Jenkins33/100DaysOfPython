# Day 34: Intermediate+ API Practice - Creating a GUI Quiz App
The Trivia API and the Quizzler App. We are going to go back to an API we worked on in Day 17 that has over 3,000 verified questions (Open Trivia Database).

This is a review for what we learned about API Endpoints, sending requests to a particular endpoint to ask for a piece of data. We're also going to be looking at what we learned about API Parameters in order to get different pieces of data from the API. With those, we're going to use Tkinter to build a Quizzler App.

A True/False question shows up in the middle with two buttons for the user to guess the answer.

## Trivia Question API Challenge

We built a question app on Day 17 when we were learning about classes. The goal now, with our newfound knowledge regarding Graphical User Interfaces and the ability to hit APIs, is to upgrade this archaic console app and give it a facelift. And enable it to be more dynamic by drawing data from an API.

`data.py` has a list of dictionary objects. At the time, this was the best we could do (we printed out the API response in the browser and copy/pasted). Hard-coded values will never change. Now, we can take it a step further to get different questions and different answers.

1. Modify the `data.py` file (don't change the `main.py`)
2. Make a `get()` request to fetch 10 True or False questions
3. Parse the JSON response and replace the value of `question_data` (don't change the variable name)

*Hint:* create a Python dictionary for the `amount` and `type` parameters

```py
import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

def get_questions():
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data['results']

question_data = get_questions()
```

## Solution & Walkthrough for getting Trivia Questions
**Instructor Code**

(Completed it almost word-for-word; just placed mine in a function.)

```py
import requests

parameters = {
  "amount": 10,
  "type": "boolean"
}

response = resposne.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]
```

## Unescaping HTML Entities
Some characters were formatted strangely in the text we were receiving from the API. We were being sent **HTML entities**; it's a way to prevent certain characters from confusing the HTML code. 

We can use [freeformatter.com](https://www.freeformatter.com/html-escape.html) to help for google direction.

Doing so will guide us to the `html` module. We'll want to use this in our `quiz_brain.py` file.

```py
import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
```

This takes you to the `intermediate++` level. Google is your best friend!

## Class based Tkinter UI
Time to upgrade the program so it has a GUI!

## Python Typing & Showing the Next Question in the GUI

## Python Typing: Type Hints and Arrows ->

## Check the Answer

## Give Feedback to the Player, Keep Score, and the Fix the Bugs =)