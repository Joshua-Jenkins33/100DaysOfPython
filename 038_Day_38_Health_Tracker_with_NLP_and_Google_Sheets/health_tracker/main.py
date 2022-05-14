import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv(r'038_Day_38_Health_Tracker_with_NLP_and_Google_Sheets\health_tracker\.env')

NUTRITION_API_KEY=os.getenv("NUTRITIONIXAPIKEY")
NUTRITION_APP_ID=os.getenv("NUTRITIONIXAPPID")
WORKOUTS_TOKEN=os.getenv("PYTHONMYWORKOUTSTOKEN")
GENDER="male"
WEIGHT=88.45
HEIGHT=180.34
AGE=27

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/f5343720735630e16f47193195b5f6d9/workouts/workouts"

exercise_headers = {
    "x-app-id": NUTRITION_APP_ID,
    "x-app-key": NUTRITION_API_KEY,
    "Content-Type": "application/json"
}

workout = input("Tell me about your workout in a sentence! (type, distance, length of time): ")

exercise_params = {
    "query": workout,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

exercise_response = requests.post(url=exercise_endpoint, json=exercise_params, headers=exercise_headers)
exercise_response.raise_for_status()

exercise_results = exercise_response.json()

now = datetime.now()
date = now.strftime("%Y/%m/%d")
time = now.strftime("%H:%M:%S")

for exercise in exercise_results["exercises"]:
  sheet_inputs = {
    "workout": {
      "date": date,
      "time": time,
      "exercise": exercise['name'].title(),
      "duration": exercise["duration_min"],
      "calories": exercise["nf_calories"]
    }
  }

  sheety_headers = {
    "Authorization": f"Bearer {WORKOUTS_TOKEN}"
  }

  sheety_response = requests.post(url=sheety_endpoint, json=sheet_inputs, headers=sheety_headers)
  sheety_response.raise_for_status()

