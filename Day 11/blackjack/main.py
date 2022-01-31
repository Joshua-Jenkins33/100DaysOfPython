from array import array
from art import logo
import random

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

def get_card():
    """Grabs a random card value from an array of card values

    Args:
        N/A
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = random.randint(0,len(cards)-1)
    return cards[drawn_card]

def get_score(points_list: list):
    """Takes in an array of points and sums them together

    Args:
        points_list (list): An array of points

    Returns:
        int: The sum of points in an input array for the player
    """
    total_points: int = 0

    for point in points_list:
        total_points += point

    return total_points

def computer_draw(computer_points: list):
    """Computer will draw until they have a score of at least 17.

    Args:
        computer_points (list): The computer's array of cards/points!
    """
    while get_score(computer_points) < 17 or len(computer_points) < 1:
        computer_points.append(get_card())
        computer_points = calculate_aces(computer_points)

    return computer_points
        
def calculate_aces(points: list):
    """If you have an ace and it would put you over the score, convert it to a 1 instead of an 11

    Args:
        points (list): A list of points
    """
    for index in range(len(points)):
        if points[index] == 11:
            if get_score(points) > 21:
                points[index] = 1

    return points

def get_results(player: list, dealer: list):
    game_results: str = ''
    if get_score(player) < 21 and get_score(dealer) > 21:
        game_results = "Opponent went over. You win! 😁"
    elif get_score(player) < 21 and get_score(dealer) < get_score(player):
        game_results = "You win! 😁"
    elif get_score(player) < 21 and get_score(dealer) > get_score(player):
        game_results = "Opponent scored more than you. You lose..."
    elif get_score(player) > 21:
        game_results = "You went over. You lose 😤"
    elif get_score(player) == get_score(dealer) and get_score(player) < 21:
        game_results = "Draw 🙃"
    elif get_score(player) == get_score(dealer) and get_score(player) == 21:
        game_results = "Lose, opponent has Blackjack 😱"
        # This probably shouldn't execute
    elif get_score(player) == 21:
        game_results = "Win with a Blackjack 😎"

    return game_results

def check_blackjack(points: list, player: str):
    blackjack = ""
    if player == "Self" and get_score(points) == 21:
        blackjack = "Win with a Blackjack 😎"
    elif player == "Dealer" and get_score(points) == 21:
        blackjack = "Lose, opponent has Blackjack 😱"
    if len(blackjack) > 1:
        return blackjack


wantsToPlay = False

if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    wantsToPlay = True

while wantsToPlay == True:
    print(logo)

    player_points: list = []
    dealer_points: list = []
    dealers_first: int = 0

    starting_round = 0
    while starting_round < 2:
        player_points.append(get_card())
        dealer_points = computer_draw(dealer_points)
        starting_round += 1

    print(f"You cards: {player_points}, current score: {get_score(player_points)}\nComputer's first card: {dealer_points[0]}")

    opponent_blackjack: str = ""
    player_blackjack: str = ""

    continue_game = True
    if get_score(dealer_points) == 21:
        opponent_blackjack = "Lose, opponent has Blackjack 😱"
        continue_game = False
    while continue_game == True:
        if get_score(player_points) == 21:
            player_blackjack = "Win with a Blackjack 😎"
            continue_game = False
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            player_points.append(get_card())
            calculate_aces(player_points)
            print(f"You cards: {player_points}, current score: {get_score(player_points)}\nComputer's first card: {dealer_points[0]}")
        else:
            continue_game = False

    print(f"Your final hand: {player_points}, final score: {get_score(player_points)}")
    print(f"Dealer's final hand: {dealer_points}, final score {get_score(dealer_points)}")
    if len(opponent_blackjack) > 1:
        print(opponent_blackjack)
    if len(player_blackjack) > 1:
        print(player_blackjack)
    print(get_results(player_points, dealer_points))


    if input("Looks like you finished your game! Would you like to play again? Type 'y' or 'n': ") == 'n':
        wantsToPlay = False

if wantsToPlay == False:
    print("Come back and play again later!")

""" 

Need to specify what happens when there's a tie. 

Need to autoclose if player goes over.
- Use the while loop to check the score

"""