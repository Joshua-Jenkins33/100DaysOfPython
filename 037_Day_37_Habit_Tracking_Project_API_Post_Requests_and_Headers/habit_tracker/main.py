import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# TODO: Separate out into functions
# TODO: Create user prompts for information

load_dotenv(r'037_Day_37_Habit_Tracking_Project_API_Post_Requests_and_Headers\habit_tracker\.env')

USERNAME=os.getenv("PIXELAUSERNAME")
TOKEN=os.getenv("TOKEN")
GRAPH_ID="graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


def create_user(user, is_new=False):
    global graph_endpoint
    global pixela_endpoint
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    if is_new:
        user_params['username'] = user
        graph_endpoint = f"{pixela_endpoint}/{user}/graphs"

    response = requests.post(url=pixela_endpoint, json=user_params)
    return response # might be good to save this in the case of a new user


def should_create_new_user() -> dict:
    decision = input("Would you like to create a new user? (yes/no): ")
    pending = True
    while pending:
        if 'y' in decision.lower():
            new_user = input("What would you like your username to be? ")
            confirmation = input(f"You entered {new_user}. Is that correct? ")
            if 'y' in confirmation.lower():
                print(f"Creating a new user with the username: {new_user}!")
                pending = False
                return {"is_new_user": True, "username": new_user}
        else:
            print(f"Alright! Using {USERNAME}, then.\n")
            pending = False
            return {"is_new_user": False, "username": USERNAME}


def create_graph():
    graph_config = {
        "id": GRAPH_ID,
        "name": "Swimming Graph",
        "unit": "Yd",
        "type": "float",
        "color": "sora"
    }

    # requests.post(url=graph_endpoint, json=graph_config)
    requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def also_create_graph_question_mark(): # deprecated
    today = datetime.now().strftime("%Y%m%d")
    body = {
        "date": today,
        "quantity": "120"
    }

    response = requests.post(url=pixel_creation_endpoint, json=body, headers=headers)
    print(response.text)


def delete_day():
    date_to_delete = input("What date would you like to delete? Format as (YYYYmmdd): ")
    requests.delete(url=f'{pixel_creation_endpoint}/{date_to_delete}', headers=headers)
    # some logic to confirm that deletion was successful


def add_swim_yardage_for_today() -> dict:
    workout_date = input("What date did you complete this workout? (format: 20200101) ")
    # today = datetime.now().strftime("%Y%m%d")
    put_url = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{workout_date}"
    update_data = {
        "date": workout_date,
        "quantity": input("How many yards did you actually swim today? ")
    }
    response = requests.put(url=put_url, json=update_data, headers=headers)
    print(response.text)
    return {
        "put_url": put_url,
        "update_data": update_data,
        "api_response": response
    }


if should_create_new_user()['is_new_user']:
    create_user(should_create_new_user()['username'], should_create_new_user()['is_new_user'])

decision = input("Would you like to:\n1. Create a new graph\n2. Add to an existing graph\n3. Delete from an existing graph?\n(valid responses are create/add/delete)\n").lower()
if decision == 'create' or decision == '1':
    create_graph() # doesn't handle custom building a graph; just uses default one
    #TODO: Handle custom building graph
elif decision == 'add' or decision == '2':
    response_data = add_swim_yardage_for_today() # doesn't handle custom adding data to a graph; just swimming
    #TODO: Handle custom graph update input
    print(response_data['put_url'])
elif decision == 'delete' or decision == '3':
    delete_day()
    #TODO: Handle custom graph deletes