from flask import Flask
from random import randint

GAME_START_GIF = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'
HIGH_GIF = 'https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'
LOW_GIF = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'
CORRECT_GIF = 'https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'

#TODO: 2. Create a new Flask application where the home route displays an <h1> that says "Guess a number between 0 and 9" and display a gif of your choice from giphy.com.
app = Flask(__name__)
print("Starting up!")
print(app)

@app.route('/')
def game_start():
    return f'<h1 style="text-align: left"> Guess a number between 0 and 9</h1> \
            <br> \
            <img src="{GAME_START_GIF}" width=200px>'


# Generate a random number between 0 and 9 or any range of numbers of your choice.
game_winning_random_number = randint(0, 9)
print(f"The Game Winning Number is: {game_winning_random_number}.")




#TODO: 4. Create a route that can detect the number entered by the user e.g "URL/3" or "URL/9" and checks that number against the generated random number. If the number is too low, tell the user it's too low, same with too high or if they found the correct number. try to make the <h1> text a different colour for each page.  e.g. If the random number was 5:
def too_low():
    return f'<h1 style="text-align: left; color: red">Too low, try again!</h1> \
            <br> \
            <img src="{LOW_GIF}" width=200px>'


def too_high():
    return f'<h1 style="text-align: left; color: purple">Too high, try again!</h1> \
            <br> \
            <img src="{HIGH_GIF}" width=200px>'


def correct():
    return f'<h1 style="text-align: left; color: green">You found me!</h1> \
            <br> \
            <img src="{CORRECT_GIF}" width=200px>'

@app.route('/<int:guess>')
def validate_guess(guess):
    if guess < game_winning_random_number:
        print("Too low")
        return too_low()
    elif guess > game_winning_random_number:
        print("Too high")
        return too_high()
    else: 
        print("You win!")
        return correct()

if __name__ == "__main__":
    app.run(debug=True)