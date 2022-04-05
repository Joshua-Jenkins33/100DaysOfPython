import turtle, pandas
from states_manager import StatesManager

screen = turtle.Screen()
screen.title("U.S. States Game")
IMAGE = r"Day_25\my_code\US_States_Game\blank_states_img.gif"
STATES_FILE = r"C:\repos\100DaysOfPython\Day_25\my_code\US_States_Game\50_states.csv"
screen.addshape(IMAGE)
turtle.shape(IMAGE)

##########################################################################################
""" USED IN GETTING COORDINATES ON A TURTLE SCREEN
def get_mouse_click_coor(x, y):
  print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
"""
##########################################################################################

correct_answers = []

#Convert the guess to Title case
def prompt_for_state():
  answer_state = screen.textinput(title=f"{len(correct_answers)}/50 | Guess the State", prompt="What's another state's name?").title()
  print(f'Answer State: {answer_state}')
  return answer_state


#Check if the guess is among the 50 states
def read_csv(file):
  df = pandas.read_csv(file)
  print(f'CSV DataFrame: {df}')
  return df


def filter_df(df, df_filter_col, df_filter_val):
  df_filtered_for_guess = df[df[df_filter_col] == df_filter_val]
  print(f'Filtered DataFrame: {df_filtered_for_guess}')
  return df_filtered_for_guess


def check_for_score(df_filtered, guessed_state):
  if len(df_filtered) > 0:
    print(f"That's right! {guessed_state} is a State!")
    write_state_to_map(df_filtered, guessed_state)
  #Record the correct guesses in a list
    correct_answers.append(guessed_state)
  else:
    print(f"Nope. There are no states named {guessed_state}.")


#Write the correct guesses onto the map
def write_state_to_map(df_filtered, state):
  state_text = state
  state_x = df_filtered['x'].values[0]
  state_y = df_filtered['y'].values[0]
  # print(f'PRINTING::: {state_text, state_x, state_y}')
  StatesManager(state_text, state_x, state_y)

#Use a loop to allow the user to keep guessing
while len(correct_answers) < 50:

  #Keep track of the score
  answer_state = prompt_for_state()
  if answer_state == "Exit":
    break
  df = read_csv(STATES_FILE)
  df_filtered = filter_df(df, 'state', answer_state)
  check_for_score(df_filtered, answer_state)

#states_to_learn.csv
all_states = df.state.to_list()
# print("Missing values in second list:", (set(all_states).difference(correct_answers)))
states_to_learn = set(all_states).difference(correct_answers)
data_dict = {
  "state": []
}

for state in states_to_learn:
  data_dict["state"].append(state)

df = pandas.DataFrame(data_dict)
df.to_csv(r'C:\repos\100DaysOfPython\Day_25\my_code\US_States_Game\states_to_learn.csv')
